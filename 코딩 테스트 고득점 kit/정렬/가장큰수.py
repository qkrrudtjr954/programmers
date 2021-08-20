from functools import cmp_to_key

def compare(x: str, y: str):
    return int(y + x) - int(x + y)

def solution(numbers):
    numbers = sorted(map(str, numbers), key=cmp_to_key(compare))
    return str(int(''.join(numbers)))
