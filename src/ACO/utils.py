import random
from typing import List, Set


def matrix_nice_str(matrix:List[List[object]]) -> str:
    return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])

def choose_best_clique(clique_1: Set[int], clique_2: Set[int]) -> Set[int]:
    if len(clique_1) > len(clique_2):
        return clique_1
    elif len(clique_1) == len(clique_2):
        return random.choice([clique_1, clique_2])

    return clique_2

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