from typing import Tuple


def union(parents, a, b):
    p1 = find(parents, a)
    p2 = find(parents, b)

    if p1 == p2:
        raise Exception('same parent')

    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2


def find(parents, node):
    if node != parents[node]:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union_find(n, u: Tuple[int, int]):
    '''
    :param n: 노드 갯수
    :param u: Union 연산 튜플
    :return parents: 루트 노드 배열
    '''
    parents = [i for i in range(n)]

    for a, b in u:
        union(parents, a, b)

    return parents
