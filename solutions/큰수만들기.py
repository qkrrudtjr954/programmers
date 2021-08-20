def get_remove_number_idx(number):
    for i in range(len(number) - 1):
        if int(number[i]) < int(number[i + 1]):
            return i


def solution(number, k):
    if k == 0 or len(number) <= 1:
        return number

    remove_num_idx = get_remove_number_idx(number)
    new_number = number[:-1] if remove_num_idx is None else number[:remove_num_idx] + number[remove_num_idx + 1:]

    return solution(new_number, k - 1)


if __name__ == '__main__':
    print(solution("4177252841", 4))
