from typing import List, Tuple

from practice.union_find import find, union
from operator import itemgetter


def kruskal(n, costs: List[Tuple[int, int, int]]):
    '''
    :param n: 노드 갯수
    :param costs: 노드 별 가중치 (시작 노드, 종착 노드, 가중치)

    :return total_cost: 최소 가중치
    '''
    parents = [i for i in range(n)]
    costs.sort(key=itemgetter(2))

    total_cost = 0

    for a_node, b_node, cost in costs:
        if find(parents, a_node) != find(parents, b_node):
            union(parents, a_node, b_node)
            total_cost += cost

    return total_cost
