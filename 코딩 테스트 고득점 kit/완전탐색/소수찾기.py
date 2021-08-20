from itertools import permutations
from math import ceil, sqrt


def fetch_all_numbers(numbers: str):
    for length in range(1, len(numbers) + 1):
        for number in permutations(numbers, length):
            yield int(''.join(number))


def get_all_prime_numbers(n):
    all_numbers = {number: True for number in range(2, n + 1)}

    for number in range(2, ceil(sqrt(n))):
        if all_numbers[number] is False:
            continue

        for none_prime_number in range(number * 2, n + 1, number):
            all_numbers[none_prime_number] = False

    return [number for number, is_prime in all_numbers.items() if is_prime]


def solution(numbers):
    all_numbers = set(fetch_all_numbers(numbers))
    all_prime_numbers = set(get_all_prime_numbers(max(all_numbers)))

    return len(all_numbers & all_prime_numbers)


if __name__ == '__main__':
    print(solution("17"))
