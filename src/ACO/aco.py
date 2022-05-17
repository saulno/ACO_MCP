from abc import ABC, abstractmethod
from typing import Set
from .Graph import Graph
from .utils import choose_best_clique


class AntColonyOptimization(ABC):

    def __init__(self, graph: Graph, tau_min: float = 0.01, tau_max: float = 6.0, alpha: float = 1.0, rho: float = 0.99) -> None:
        super().__init__()
        self.graph = graph
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.alpha = alpha
        self.rho = rho

        self.pheromones = self.set_initial_pheromone_trails()

    @abstractmethod
    def set_initial_pheromone_trails(self):
        ...

    @abstractmethod
    def tau_factor_of_vertex(self, vertex: int, current_clique: Set[int]) -> float:
        ...

    @abstractmethod
    def increment_pheromone(self, pheromone_quantity: float, current_clique: Set[int]):
        ...
    
    @abstractmethod
    def decrement_pheromone(self):
        ...

    def choose_vertex_uisng_pheromone_probabilities(self, candidates: Set[int], current_clique: Set[int]) -> int:
        def prob(vertex: int) -> float:
            p = self.tau_factor_of_vertex(vertex, current_clique) ** self.alpha 
            p /= sum([self.tau_factor_of_vertex(c, current_clique) for c in candidates])
            return p

        probabilities = [(prob(c), c) for c in candidates]

        # Return random based in probabilitites
        return max(probabilities)[1]

    def update_pheromone_trails(self, best_clique: Set[int], k_clique: Set[int]):
        self.decrement_pheromone()
        pheromone_quantity = 1 / (1 + len(best_clique) - len(k_clique))
        self.increment_pheromone(pheromone_quantity, k_clique)

    def aco_procedure(self, k_ants: int, generations: int) -> Set[int]:

        print("===========  clique ACO ==============")

        global_best_clique = set()

        for g in range(generations):
            generation_best_clique = set()

            for k in range(k_ants):
                initial_vertex = self.graph.select_random_vertex()
                k_clique = {initial_vertex}
                candidates = self.graph.get_neighbor_candidates(initial_vertex)
                
                while len(candidates) > 0:
                    # print(f"    Candidates {k}: |{len(candidates)}| -> {candidates}")
                    new_v = self.choose_vertex_uisng_pheromone_probabilities(candidates, k_clique)
                    k_clique.add(new_v)
                    new_v_candidates = self.graph.get_neighbor_candidates(new_v)
                    candidates = candidates.intersection(new_v_candidates)

                # print(f"  Ant {k}: |{len(k_clique)}| -> {k_clique}")
                generation_best_clique = choose_best_clique(generation_best_clique, k_clique)

            global_best_clique = choose_best_clique(global_best_clique, generation_best_clique)
            self.update_pheromone_trails(global_best_clique, generation_best_clique)
            
            print(f"Generation {g}: |{len(generation_best_clique)}| -> {generation_best_clique}")
        
        return global_best_clique


    def __str__(self) -> str:
        msg = "Ant Colony Optimization\n"
        msg += f"    tau min: {self.tau_max}\n"
        msg += f"    tau max: {self.tau_min}\n"
        msg += f"    alpha:   {self.alpha}\n"
        msg += f"    rho:     {self.rho}\n"

        return msg