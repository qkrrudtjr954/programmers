from functools import reduce
from collections import Counter

def solution(clothes):
    # 의상 종류별 의상의 갯수를 구한다.
    count = Counter(category for _, category in clothes)

    # 의상 갯수별 경우의 수를 구한다.
    # headgear: 2  2개를 각각 쓸 확률 2 + 하나도 안쓸 확률 1 = 3
    # eyewear:  1  1개를 각각 쓸 확률 1 + 하나도 안쓸 확률 1 = 2
    # 총 6개 - 모두 안쓸 확률 1 = 총 5개
    return reduce(lambda x, y: x * y, map(lambda v: v + 1, count.values())) - 1
