def mark_visited(root, adjacent, visited):
    stack = [root]

    while len(stack) != 0:
        idx = stack.pop()
        visited[idx] = True

        for n in adjacent[idx]:
            if visited[n]:
                continue
            else:
                stack.append(n)


def solution(n, computers):
    adjacent = [[] for _ in range(n)]

    for i in range(n):
        for j in range(i):
            if computers[i][j] == 1:
                adjacent[i].append(j)
                adjacent[j].append(i)

    visited = [False] * n

    answer = 0

    while not all(visited):
        root = next(idx for idx, v in enumerate(visited) if v is False)
        mark_visited(root, adjacent, visited)
        answer += 1

    return answer


if __name__ == '__main__':
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
