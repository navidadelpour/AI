import random
import math
from pprint import pprint

class GA:

    population = []
    p_crossover = .3;
    p_mutation = .1;

    def __init__(self):
        for _ in range(10):
            x = round(random.uniform(-5, 5), 2)
            y = round(random.uniform(-5, 5), 2)
            f = self.F(x, y)
            self.population.append(((x, y), f))

        self.population = sorted(self.population, key = lambda x: x[1])
        pprint(self.population)

        for i in range(2):
            print("==========================================================================")
            new_population = []
            for i in [0, 2, 4, 6, 8]:
                n = self.population[i]
                m = self.population[i + 1]
                if random.uniform(0, 1) < self.p_crossover:
                    for j in [0, 1]:
                        x = self.population[i + j][0][0]
                        y = self.population[i + 1 - j][0][1]
                        f = self.F(x, y)
                        new_population.append(((x, y), f))
                else:
                    new_population.append(n)
                    new_population.append(m)

            i = 0
            for p in new_population:
                if random.uniform(0, 1) < self.p_mutation:
                    x = round(p[0][0] + random.uniform(-1, 1), 2)
                    y = round(p[0][1] + random.uniform(-1, 1), 2)
                    f = self.F(x, y)
                    new_population[i] = ((x, y), f)
                i += 1
            self.population = new_population

            self.population = sorted(self.population, key = lambda x: x[1])
            pprint(self.population)

    def F(self, x, y):
        return round(-20.0 * math.exp(-.2 * math.sqrt(.5) * math.hypot(x, y)) - math.exp(.5 * (math.cos(2.0 * x * math.pi) + math.cos(2.0 * y * math.pi))) + 20.0 + 0.01, 2)


g = GA()