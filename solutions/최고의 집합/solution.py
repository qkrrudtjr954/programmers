from icecream import ic


def solution(n, s):
    if n > s:
        return [-1]

    answer = [int(s / n)] * n
    remain = s - sum(answer)

    idx = 0

    while remain > 0:
        answer[idx] += 1
        remain -= 1
        idx += 1
        if idx == n:
            idx -= n

    return sorted(answer)


if __name__ == '__main__':
    ic(solution(3, 9))
    ic(solution(9, 100000000))
    ic(solution(2, 8))
    ic(solution(2, 9))
