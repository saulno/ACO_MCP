from typing import Set
from .Graph import Graph
from .ACO import AntColonyOptimization


class VertexAC(AntColonyOptimization):
    def __init__(self, graph: Graph, tau_min: float = 0.01, tau_max: float = 6.0, alpha: float = 1.0, rho: float = 0.99) -> None:
        super().__init__(graph, tau_min, tau_max, alpha, rho)

    def set_initial_pheromone_trails(self):
        return [self.tau_max for _ in range(self.graph.number_vertex)]

    def tau_factor_of_vertex(self, vertex: int, current_cliqe: Set[int]) -> float:
        return self.pheromones[vertex]
    
    def increment_pheromone(self, pheromone_quantity: float, current_clique: Set[int]):
        for v in current_clique:
            self.pheromones[v] += pheromone_quantity
    
    def decrement_pheromone(self):
        self.pheromones = [self.rho * p for p in self.pheromones]

    def __str__(self) -> str:
        msg = "Vertex AC (Ant Clique) variant\n"
        msg += super().__str__() 
        msg += f"  Pheromone trail: \n{self.pheromones}"

        return msg

