import random
from deap import creator, base, tools, algorithms
from CandidateSolutionEvaluator import CandidateSolutionEvaluator


addresses = [
    '1600 Pennsylvania Avenue, Washington DC 20006',
    '11 Wall Street New York, NY 10005',
    'New York, NY 10004',
    '4059 Mt Lee Dr. Hollywood, CA 90068',
    '1025 N Broadway, Milwaukee, WI 53202',
    '600 E Fremont St, Las Vegas, NV 89101',
    '17135 W. Bluemound Rd. Brookfield, WI 53005-5915',
    '2455 Telegraph Ave. Berkeley, CA 94704',
]


class Program:
    def __init__(self):
        pass

    @staticmethod
    def main():
        evaluator = CandidateSolutionEvaluator(addresses)
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("attr_index", Program.random_indexes)
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.attr_index)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", evaluator.evaluate)
        toolbox.register("mate", tools.cxOrdered)
        toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=100)

        hof = tools.HallOfFame(maxsize=1)
        final_population = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.5, ngen=250, halloffame=hof)

        print(f"Final population: {final_population}")
        best_solution = hof[0]
        print(f"Best solution: {best_solution}, fitness: {best_solution.fitness}")
        print("The solution addresses in order are:\n*************************")
        for address_index in best_solution:
            print(addresses[address_index])
        print("*************************")
        print(f"Total miles: {best_solution.fitness}")

    @staticmethod
    def random_indexes():
        non_random_indexes = list(range(len(addresses)))
        random.shuffle(non_random_indexes)
        return non_random_indexes


if __name__ == "__main__":
    Program.main()
