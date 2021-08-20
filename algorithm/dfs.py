from dataclasses import dataclass, field
from typing import List

from icecream import ic

stack = list()


@dataclass
class Node:
    data: int
    adjacent: List['Node'] = field(default_factory=list)
    marked: bool = field(default=False)


@dataclass
class Graph:
    def __init__(self, size):
        self.nodes = [Node(data=i) for i in range(size)]

    def add_edge(self, i1, i2):
        node1 = self.nodes[i1]
        node2 = self.nodes[i2]

        if node1 not in node2.adjacent:
            node2.adjacent.append(node1)

        if node2 not in node1.adjacent:
            node1.adjacent.append(node2)

    def dfs(self, i=0):
        node = self.nodes[i]
        node.marked = True

        stack.append(node)

        while len(stack) > 0:
            r = stack.pop()
            for n in r.adjacent:
                if n.marked:
                    continue
                else:
                    n.marked = True
                    stack.append(n)
            ic(r.data)


if __name__ == '__main__':
    graph = Graph(9)
    graph.add_edge(0, 1)

    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)

    graph.add_edge(2, 1)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)

    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 4)
    graph.add_edge(3, 5)

    graph.add_edge(4, 2)
    graph.add_edge(4, 3)

    graph.add_edge(5, 3)
    graph.add_edge(5, 6)
    graph.add_edge(5, 7)

    graph.add_edge(6, 5)
    graph.add_edge(6, 8)

    graph.add_edge(7, 5)

    graph.add_edge(8, 6)

    graph.dfs()
