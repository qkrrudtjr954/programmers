from math import ceil, sqrt


def solution(brown, yellow):
    총_격자_수 = brown + yellow

    for 가로_격자_수 in range(ceil(sqrt(총_격자_수)), brown // 2):
        if 총_격자_수 % 가로_격자_수 != 0:
            continue

        세로_격자_수 = 총_격자_수 // 가로_격자_수
        테두리_격자_수 = (가로_격자_수 * 2) + (세로_격자_수 * 2) - 4

        if 테두리_격자_수 == brown:
            return [가로_격자_수, 세로_격자_수]


if __name__ == '__main__':
    print(solution(10, 2))
    print(solution(8, 1))
