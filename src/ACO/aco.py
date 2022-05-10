from abc import ABC, abstractmethod
from .graph import Graph


class AntColonyOptimization(ABC):

    def __init__(self, g: Graph, tau_min: float = 0.01, tau_max: float = 6.0, alpha: float = 1.0, rho: float = 0.99) -> None:
        super().__init__()
        self.g = g
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.alpha = alpha
        self.rho = rho

        self.pheromones = self.set_initial_pheromone_trails()

    @abstractmethod
    def set_initial_pheromone_trails(self):
        ...

    def __str__(self) -> str:
        msg = "Ant Colony Optimization\n"
        msg += f"    tau min: {self.tau_max}\n"
        msg += f"    tau max: {self.tau_min}\n"
        msg += f"    alpha:   {self.alpha}\n"
        msg += f"    rho:     {self.rho}\n"

        return msg