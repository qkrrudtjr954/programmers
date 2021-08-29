def solution1(n, works):
    if sum(works) <= n:
        return 0

    for i in range(n):
        works[works.index(max(works))] -= 1

    return sum(map(lambda w: w * w, works))


def solution2(n, works):
    if sum(works) <= n:
        return 0

    work_matrix = []

    for work in works:
        l1 = [1] * work
        l2 = [0] * (max(works) - work)
        work_matrix.append(l1 + l2)

    for j in range(max(works) - 1, -1, -1):
        for i in range(len(works)):
            if n == 0:
                break

            if work_matrix[i][j] == 1:
                work_matrix[i][j] = 0
                n -= 1

        if n == 0:
            break

    return sum(map(lambda w: w * w, map(sum, work_matrix)))


def solution3(n, works):
    if sum(works) <= n:
        return 0

    work_matrix = []

    max_work = max(works)

    for w in range(max_work):
        l = []
        for work in works:
            l.append(1 if work > 0 else 0)
        work_matrix.append(l)
        works = list(map(lambda w: w - 1, works))

    work_matrix.reverse()

    for work in work_matrix:
        if n == 0:
            break

        for i in range(len(work)):
            if n == 0:
                break

            n -= work[i]
            work[i] = 0

    works = [0] * len(work_matrix[0])

    for work in work_matrix:
        for i in range(len(work)):
            works[i] += work[i]

    return sum(map(lambda w: w * w, works))


import heapq


def solution4(n, works):
    if sum(works) <= n:
        return 0

    works = [(-w, w) for w in works]

    heapq.heapify(works)

    for _ in range(n):
        _, work = heapq.heappop(works)
        work -= 1
        heapq.heappush(works, (-work, work))

    return sum(map(lambda w: w * w, [w for _, w in works]))
