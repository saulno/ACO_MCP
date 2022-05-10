from .graph import Graph
from .ACO import AntColonyOptimization


class VertexAC(AntColonyOptimization):
    def __init__(self, g: Graph, tau_min: float = 0.01, tau_max: float = 6.0, alpha: float = 1.0, rho: float = 0.99) -> None:
        super().__init__(g, tau_min, tau_max, alpha, rho)

    def set_initial_pheromone_trails(self):
        return []

    def __str__(self) -> str:
        msg = "Vertex AC (Ant Clique) variant\n"
        msg += super().__str__() 

        return msg

