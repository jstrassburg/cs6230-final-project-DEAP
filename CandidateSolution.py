class CandidateSolution:
    size = 4  # TODO: this is fake

    def __init__(self, bits=None):
        if bits is None:
            pass  # TODO: initialize new
        else:
            self.decode(bits)

    def decode(self, bits):
        pass  # TODO: Decode the bits into the coordinates of the trip

    @staticmethod
    def evaluate(bits):
        candidate = CandidateSolution(bits)
        distance = 0.0  # TODO: Calculate total distance using geopy
        return sum(bits),  # this has to be a tuple
