from tenacity import retry, stop_after_attempt
from geopy import geocoders, distance


class CandidateSolutionEvaluator:
    def __init__(self, addresses):
        geocoders.options.default_timeout = 10
        self._geo_locator = geocoders.Nominatim(user_agent='cs6230-final-project')
        self._locations = [self.address_to_coordinates(address) for address in addresses]

    def evaluate(self, chromosome):
        address_count = len(chromosome)
        if address_count < 2:
            raise "Must be evaluating at least 2 addresses."
        total_distance = 0.0
        for i in range(len(chromosome)-1):
            first = self._locations[chromosome[i]]
            second = self._locations[chromosome[i+1]]
            total_distance += distance.distance(first.point, second.point).miles
        # Now, do the loop around back to the first location
        first = self._locations[-1]
        second = self._locations[0]
        total_distance += distance.distance(first.point, second.point).miles

        return total_distance,  # This is a tuple to support multi-objective GA's

    @retry(stop=stop_after_attempt(5))
    def address_to_coordinates(self, address):
        print(f"Looking up coordinates for: {address}")
        location = self._geo_locator.geocode(address)
        if not location:
            raise f"Address not found: {address}"
        return location
