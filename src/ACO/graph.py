import random
from typing import List, Set

from .utils import matrix_nice_str, parse_graph_file

class Graph:

    def __init__(self, random_seed: int, filename: str) -> None:
        self.adj_mtx, self.edges_dict = parse_graph_file(filename)
        self.number_vertex = len(self.adj_mtx)

        random.seed(random_seed)

    def is_edge(self, v1: int, v2: int) -> bool:
        return self.adj_mtx[v1][v2] > 0

    def select_random_vertex(self) -> int:
        return random.choice([i for i in range(self.number_vertex)])

    def get_neighbor_candidates(self, v: int) -> Set[int]:
        return self.edges_dict[v]

    def __str__(self) -> str:
        return str(matrix_nice_str(self.adj_mtx))