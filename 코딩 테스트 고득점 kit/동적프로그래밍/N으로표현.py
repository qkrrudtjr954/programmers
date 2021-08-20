from math import ceil

MAX = 8
results = [set() for _ in range(MAX)]


def calculate(iter1, iter2):
    _results = set()
    from itertools import product
    for n1, n2 in product(iter1, iter2):
        _results.add(n1 + n2)
        _results.add(n1 * n2)
        _results.add(n1 - n2)
        _results.add(n2 - n1)
        if n2 != 0:
            _results.add(n1 // n2)
        if n1 != 0:
            _results.add(n2 // n1)
    return _results


def solution(N, number):
    for number_use_count in range(1, MAX + 1):
        index = number_use_count - 1

        if number_use_count == 1:
            results[index].add(N)

        else:
            results[index].add(int(str(N) * number_use_count))

            if number_use_count == 2:
                results[index] |= calculate(results[0], results[0])

            else:
                pivot = ceil(index / 2)
                for i1, i2 in zip(range(0, pivot, 1), range(index - 1, pivot - 1, -1)):
                    results[index] |= calculate(results[i1], results[i2])

        if number in results[index]:
            return number_use_count

    return -1
