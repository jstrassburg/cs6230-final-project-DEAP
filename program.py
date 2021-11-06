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
        chromosome_length = evaluator.get_chromosome_length()
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("attr_bool", random.randint, 0, 1)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, chromosome_length)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", evaluator.evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=100)

        hof = tools.HallOfFame(maxsize=1)
        final_population = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.1, ngen=500, halloffame=hof)

        print(f"Final population: {final_population}")
        best_solution = hof[0]
        print(f"Best solution: {best_solution}, fitness: {best_solution.fitness}")
        solution_addresses = evaluator.decode_chromosome_to_address_list(best_solution)
        print("The solution addresses in order are:\n*************************")
        for solution_address in solution_addresses:
            print(solution_address)
        print("*************************")
        print(f"Total miles: {best_solution.fitness}")


if __name__ == "__main__":
    Program.main()
