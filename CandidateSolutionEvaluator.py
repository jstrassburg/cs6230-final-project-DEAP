from BinaryConverter import BinaryConverter
from tenacity import retry, stop_after_attempt
from geopy import geocoders, distance


class CandidateSolutionEvaluator:
    def __init__(self, addresses):
        geocoders.options.default_timeout = 10
        self._geo_locator = geocoders.Nominatim(user_agent='cs6230-final-project')

        self._bits_per_address = BinaryConverter.bits_needed(len(addresses))
        self._total_chromosome_length = self._bits_per_address * len(addresses)
        self._locations = [self.address_to_coordinates(address) for address in addresses]

    def get_chromosome_length(self):
        return self._total_chromosome_length

    def evaluate(self, chromosome):
        address_indexes = self.decode_chromosome_to_indices(chromosome)
        if len(address_indexes) < 2:
            raise "Must be evaluating at least 2 addresses."
        total_distance = 0.0
        for address_index in address_indexes:
            if address_index < len(address_indexes) - 1:
                first = self._locations[address_index]
                second = self._locations[address_index + 1]
                total_distance += distance.distance(first.point, second.point).miles
        # Now, do the loop around back to the first location
        first = self._locations[-1]
        second = self._locations[0]
        total_distance += distance.distance(first.point, second.point).miles

        return total_distance,  # This is a tuple to support multi-objective GA's

    def decode_chromosome_to_address_list(self, chromosome):
        address_indexes = self.decode_chromosome_to_indices(chromosome)
        return [self._locations[index] for index in address_indexes]

    def decode_chromosome_to_indices(self, bits):
        address_indexes_binary = BinaryConverter.chunk_list(bits, self._bits_per_address)
        address_indexes = [
            BinaryConverter.binary_list_to_int(binary_address) for binary_address in address_indexes_binary]
        return address_indexes

    @retry(stop=stop_after_attempt(5))
    def address_to_coordinates(self, address):
        print(f"Looking up coordinates for: {address}")
        location = self._geo_locator.geocode(address)
        if not location:
            raise f"Address not found: {address}"
        return location
