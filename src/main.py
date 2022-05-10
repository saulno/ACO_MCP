import random
import sys
from typing import List

from ACO.graph import Graph
from ACO.EdgeAC import EdgeAC
from ACO.VertexAC import VertexAC


def main(args: List[str]):

    random_seed = 67441
    random.seed(random_seed)

    g = Graph(random_seed=random_seed, filename=args[0])

    edge_ac = EdgeAC(g)
    vertex_ac = VertexAC(g)

    print(edge_ac)
    print(vertex_ac)

if __name__ == "__main__":
    main(sys.argv[1:])
