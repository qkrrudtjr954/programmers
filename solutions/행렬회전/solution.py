# import math
#
#
# def solution(rows, columns, queries):
#     # 행렬을 초기화 한다.
#     matrix = [[0] * columns for _ in range(rows)]
#
#     for i in range(rows):
#         for j in range(columns):
#             matrix[i][j] = i * columns + (j + 1)
#
#     answer = []
#
#     for x1, y1, x2, y2 in queries:
#         # 배열 인덱스를 위해 1씩 빼준다.
#         x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
#
#         min_value = math.inf
#
#         # 북 이동
#         temp = matrix[x1][y1:y2 + 1]
#
#         for idx, y in enumerate(range(y1 + 1, y2 + 1)):
#             matrix[x1][y] = temp[idx]
#
#         min_value = min(min_value, *temp)
#
#         # 동 이동
#         temp = [temp[-1]] + [matrix[x][y2] for x in range(x1 + 1, x2 + 1)]
#
#         for idx, x in enumerate(range(x1 + 1, x2 + 1)):
#             matrix[x][y2] = temp[idx]
#
#         min_value = min(min_value, *temp)
#
#         # 남 이동
#         temp = matrix[x2][y1:y2] + [temp[-1]]
#
#         for idx, y in enumerate(range(y1, y2)):
#             matrix[x2][y] = temp[idx + 1]
#
#         min_value = min(min_value, *temp)
#
#         # 서 이동
#         temp = [matrix[x][y1] for x in range(x1, x2)] + [temp[0]]
#
#         for idx, x in enumerate(range(x1, x2)):
#             matrix[x][y1] = temp[idx + 1]
#
#         min_value = min(min_value, *temp)
#
#         answer.append(min_value)
#
#     return answer
#
#
# if __name__ == '__main__':
#     solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
#     solution(2, 2, [[1, 1, 2, 2]])
#     # assert solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]) == [8, 10, 25]


def solution(rows, columns, queries):
    # 행렬을 초기화 한다.
    matrix = [[0] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = i * rows + (j + 1)

    answer = []

    for x1, y1, x2, y2 in queries:
        # 배열 인덱스를 위해 1씩 빼준다.
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        temp = matrix[x1][y1]
        min_value = temp

        # 왼쪽 배열 위로 이동
        for x in range(x1, x2):
            current_value = matrix[x][y1]
            matrix[x][y1] = matrix[x + 1][y1]
            min_value = min(min_value, current_value)

        # 아래쪽 배열 좌로 이동
        for y in range(y1, y2):
            current_value = matrix[x2][y]
            matrix[x2][y] = matrix[x2][y + 1]
            min_value = min(min_value, current_value)

        # 오른쪽 배열 아래로 이동
        for x in range(x2, x1, -1):
            current_value = matrix[x][y2]
            matrix[x][y2] = matrix[x - 1][y2]
            min_value = min(min_value, current_value)

        # 위쪽 배열 오른쪽으로 이동
        for y in range(y2, y1, -1):
            current_value = matrix[x1][y]
            matrix[x1][y] = matrix[x1][y - 1]
            min_value = min(min_value, current_value)

        matrix[x1][y1 + 1] = temp
        answer.append(min_value)

    return answer


if __name__ == '__main__':
    print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
    print(solution(2, 2, [[1, 1, 2, 2]]))
