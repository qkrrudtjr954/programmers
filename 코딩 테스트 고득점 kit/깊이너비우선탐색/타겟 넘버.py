from collections import Counter
from itertools import chain


def solution(numbers, target):
    nodes = [0]

    for number in numbers:
        nodes = list(chain.from_iterable([(item + number, item - number) for item in nodes]))

    return Counter(nodes)[target]

