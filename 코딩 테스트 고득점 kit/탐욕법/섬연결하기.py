# kruskal 알고리즘 풀이를 그대로 사용했습니다.
from operator import itemgetter


def union(parents, a, b):
    p1 = find(parents, a)
    p2 = find(parents, b)

    if p1 < p2:
        parents[p2] = p1
    else:
        parents[p1] = p2


def find(parents, node):
    if node != parents[node]:
        parents[node] = find(parents, parents[node])
    return parents[node]


def solution(n, costs):
    costs.sort(key=itemgetter(2))

    parents = [i for i in range(n)]

    answer = 0

    for a, b, cost in costs:
        if find(parents, a) != find(parents, b):
            union(parents, a, b)
            answer += cost

    return answer


if __name__ == '__main__':
    print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
