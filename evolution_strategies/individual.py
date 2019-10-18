from abc import abstractmethod, ABC

class Individual(ABC):
    """ This class represents a single individual in the evolution strategy """
    def __init__(self, solution, s={}, fit_fun=(lambda _: 0)):
        self.solution = solution
        self.s = s
        self.fitness = fit_fun(solution)

    @abstractmethod
    def mutate_s(self):
        pass

    @abstractmethod
    def mutate_solution(self):
        pass

    @abstractmethod
    def recombine(self, Poblation):
        pass