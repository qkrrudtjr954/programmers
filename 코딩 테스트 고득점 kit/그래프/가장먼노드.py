from queue import Queue

INF = 10000000


def solution(n, edge):
    edge = list(map(lambda i: [i[0] - 1, i[1] - 1], edge))
    nodes = [[] for _ in range(n)]

    for node, adjacent in edge:
        nodes[node].append(adjacent)
        nodes[adjacent].append(node)

    visit = [True] + [False] * (n - 1)
    moves = [0] + [INF] * (n - 1)

    q = Queue()
    q.put(0)

    while not all(visit):
        current_node = q.get()

        for adjacent in nodes[current_node]:
            if visit[adjacent]:
                continue

            visit[adjacent] = True
            moves[adjacent] = moves[current_node] + 1

            q.put(adjacent)

    return moves.count(max(moves))


if __name__ == '__main__':
    from icecream import ic

    p = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    ic(solution(*p))
    p = 4, [[1, 2], [1, 3], [4, 3]]
    ic(solution(*p))
    p = 7, [[1, 2], [1, 5], [2, 4], [3, 4], [3, 5], [4, 6], [5, 7]]
    ic(solution(*p))
