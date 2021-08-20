from operator import itemgetter
from typing import List

INF = 100000


def _get_smallest_node_from(visited, distances):
    unvisited_nodes = [[node, distance] for node, (visit, distance) in enumerate(zip(visited, distances)) if not visit]

    if not unvisited_nodes:
        return

    smallest_node = min(unvisited_nodes, key=itemgetter(1))
    return smallest_node[0]


def dijkstra(n, node_distances: List[List[int, int, int]], start: int):
    '''
    :param n: 노드 갯수
    :param node_distances: 노드별 거리 정보 (시작 노드, 종착 노드, 거리)
    :param start: 시작 노드
    :return distances: 시작 노드 부터 각 노드까지의 최단 거리
    '''
    visited = [False] * (n - 1)
    distances = [INF] * n

    distances[start] = 0

    current_node = start

    while not all(visited):
        visited[current_node] = True

        for node, distance in node_distances[current_node]:
            if distances[node] > distances[current_node] + distance:
                distances[node] = distances[current_node] + distance

        current_node = _get_smallest_node_from(visited=visited, distances=distances)

    return distances
