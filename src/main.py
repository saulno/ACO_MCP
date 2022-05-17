import random
import sys
from typing import List

from ACO.Graph import Graph
from ACO.EdgeAC import EdgeAC
from ACO.VertexAC import VertexAC


def main(args: List[str]):

    random_seed = random.random() * 10000
    random.seed(random_seed)

    g = Graph(random_seed=random_seed, filename=args[0])

    edge_ac = EdgeAC(graph=g)
    vertex_ac = VertexAC(graph=g)

    print(g)

    c1 = edge_ac.aco_procedure(30, 100)
    print(c1)
    c2 = vertex_ac.aco_procedure(30, 100)
    print(c2)


if __name__ == "__main__":
    main(sys.argv[1:])
