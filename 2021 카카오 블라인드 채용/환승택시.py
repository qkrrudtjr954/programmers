INF = 200 * 100000


def solution(n, s, a, b, fares):
    '''
    n 지점의 개수    3 <= n <=200
    s 출발 지점     1 <= s <= n
    a A의 도착지점   1 <= a <= n
    b B의 도착지점   1 <= b <= n
    '''
    distances = [[INF for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            distances[i][i] = 0

    for c, d, f in fares:
        distances[c - 1][d - 1] = f
        distances[d - 1][c - 1] = f

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    answer = INF

    for k in range(n):
        answer = min(answer, distances[s - 1][k] + distances[k][a - 1] + distances[k][b - 1])

    return answer
