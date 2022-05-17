from typing import Set
from .ACO import AntColonyOptimization
from .Graph import Graph
from .utils import matrix_nice_str


class EdgeAC(AntColonyOptimization):
    def __init__(self, graph: Graph, tau_min: float = 0.01, tau_max: float = 6.0, alpha: float = 1.0, rho: float = 0.99) -> None:
        super().__init__(graph, tau_min, tau_max, alpha, rho)

    def set_initial_pheromone_trails(self):
        return [ 
            [self.tau_max if self.graph.adj_mtx[i][j] > 0 else 0 
            for j in range(len(self.graph.adj_mtx[i]))
        ] for i in range(len(self.graph.adj_mtx))]

    def tau_factor_of_vertex(self, vertex: int, current_clique: Set[int]) -> float:
        return sum([self.pheromones[vertex][c] for c in current_clique])
    
    def increment_pheromone(self, pheromone_quantity: float, current_clique: Set[int]):
        # Acotarlo a tau_min y tau_max
        for v1 in current_clique:
            for v2 in current_clique:
                if v1 != v2:
                    self.pheromones[v1][v2] += pheromone_quantity
    
    def decrement_pheromone(self):
        self.pheromones = [[self.rho * p for p in row] for row in self.pheromones]

    def __str__(self) -> str:
        msg = "Edge AC (Ant Clique) variant\n"
        msg += super().__str__() 
        msg += f"  Pheromone trail: \n{matrix_nice_str(self.pheromones)}"

        return msg

