import random
from typing import List

class Graph:

    def __init__(self, random_seed: int, filename: str) -> None:
        self.adj_mtx, self.edges_dict = parse_graph_file(filename)
        self.number_vertex = len(self.adj_mtx)

        random.seed(random_seed)

    def is_edge(self, v1: int, v2: int) -> bool:
        return self.adj_mtx[v1][v2] > 0

    def select_random_vertex(self) -> int:
        return random.choice([i for i in range(self.number_vertex)])

    def __str__(self) -> str:
        return str(self.edges_dict)

def parse_graph_file(filename: str) -> List[List[int]]:
    adj_mtx = []
    edges_dict = {}
    with open(filename, 'r') as file:
        # avoid header
        file.readline()
        
        # dimensions of the graph 
        [v1, v2, edges] = map(int, file.readline().split(" "))
        
        # read edges
        adj_mtx = [[0 for _ in range(v2)] for _ in range(v1)]
        edges_dict = {i: set() for i in range(v1)}
        for _ in range(edges):
            [i, j] = map(lambda x : int(x)-1, file.readline().split(" "))
            adj_mtx[i][j] = 1
            adj_mtx[j][i] = 1
            edges_dict[i].add(j)
            edges_dict[j].add(i)

    return adj_mtx, edges_dict