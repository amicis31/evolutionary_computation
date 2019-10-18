import numpy as np
from abc import ABC, abstractmethod

class EvolutionStrategy:
    """ This class represents the Evolution Strategy Algorithm Template """

    def __init__(self, individual_class):
        self.Individual = individual_class

    @abstractmethod
    def happy(self):
        pass

    @abstractmethod
    def by_age(self):
        # Return True if the individual is at the right age, False otherwise.
        pass

    def evolution_strategy(self, n, lam, f):
        x = np.random.random(n)
        s = {}
        current_individual = self.Individual(x, s, f(s))
        P = []
        while not self.happy():
            for _ in range(1, lam + 1):
                s_k = current_individual.mutate_s()
                x_k = current_individual.mutate_solution()
                P.append(self.Individual(x_k, s_k, f(x_k)))
            P = list(filter(self.by_age(), P))
            current_individual.recombine( P )

