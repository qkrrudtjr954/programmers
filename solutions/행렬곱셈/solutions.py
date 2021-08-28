def rotation_90_degree(arr):
    row = len(arr)
    col = len(arr[0])

    new_arr = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            new_arr[j][i] = arr[i][j]

    return new_arr


def solution(arr1, arr2):
    # arr2 = rotation_90_degree(arr2)
    arr2 = list(zip(*arr2))

    row = len(arr1)
    col = len(arr2[0])

    answer = [[0] * col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            answer[i][j] = sum(a * b for a, b in zip(arr1[i], arr2[j]))

    return answer


if __name__ == '__main__':
    # print([[1, 4], [3, 2], [4, 1]], list(zip(*[[1, 4], [3, 2], [4, 1]])))
    assert solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]) == [[15, 15], [15, 15], [15, 15]]
    assert solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]) == [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
