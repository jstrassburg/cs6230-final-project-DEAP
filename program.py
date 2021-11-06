import random
from deap import creator, base, tools, algorithms
from CandidateSolution import CandidateSolution


class Program:
    def __init__(self):
        pass

    @staticmethod
    def main():
        creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMin)

        toolbox = base.Toolbox()
        toolbox.register("attr_bool", random.randint, 0, 1)
        toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, CandidateSolution.size)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        toolbox.register("evaluate", CandidateSolution.evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
        toolbox.register("select", tools.selTournament, tournsize=3)

        population = toolbox.population(n=10)

        hof = tools.HallOfFame(maxsize=1)
        final_population = algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.1, ngen=10, halloffame=hof)

        print(final_population)
        print(f"Best solution: {hof[0]}, fitness: {hof[0].fitness}")

        best_solution = CandidateSolution(hof[0])
        print(f"The best solution was: {best_solution} distance TODO.")


if __name__ == "__main__":
    Program.main()
