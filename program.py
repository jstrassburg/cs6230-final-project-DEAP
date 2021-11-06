import random
from deap import creator, base, tools, algorithms
from CandidateSolution import CandidateSolution
from BinaryConverter import BinaryConverter

places = [
    '1600 Pennsylvania Avenue, Washington DC 20006',
    '11 Wall Street New York, NY 10005',
    '350 Fifth Avenue New York, NY 10118',
    '4059 Mt Lee Dr. Hollywood, CA 90068',
    '1025 N Broadway, Milwaukee, WI 53202',
    '600 E E Fremont St, Las Vegas, NV 89101',
    '17135 W. Bluemound Rd. Brookfield, WI 53005-5915',
    '2455 Telegraph Ave. Berkeley, CA 94704',
]


class Program:
    def __init__(self):
        pass

    @staticmethod
    def main():
        bits_needed = BinaryConverter.bits_needed(len(places))
        total_chromosome_length = bits_needed * len(places)

        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("attr_bool", random.randint, 0, 1)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, total_chromosome_length)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", CandidateSolution.evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=50)

        hof = tools.HallOfFame(maxsize=1)
        final_population = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.1, ngen=10, halloffame=hof)

        print(final_population)
        print(f"Best solution: {hof[0]}, fitness: {hof[0].fitness}")


if __name__ == "__main__":
    Program.main()
