import random
import sys
from typing import List

from ACO.aco import aco
from ACO.graph import Graph


def main(args: List[str]):
    print("hello world")

    random_seed = 67441

    random.seed(random_seed)
    g = Graph(random_seed=random_seed, filename=args[0])

    print(g)
    aco()

if __name__ == "__main__":
    main(sys.argv[1:])
