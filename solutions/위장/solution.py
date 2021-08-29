from collections import Counter
from functools import reduce


def solution(clothes):
    return reduce(lambda a, b: a * b, list(map(lambda v: v + 1, Counter([c for _, c in clothes]).values()))) - 1


if __name__ == '__main__':
    assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
