# from icecream import ic
#
#
# def separate_triangle(triangle):
#     left_triangle = []
#     right_triangle = []
#
#     for h in range(1, len(triangle)):
#         l = []
#         r = []
#         for w in range(len(triangle[h]) - 1):
#             l.append(triangle[h][w])
#             r.append(triangle[h][w + 1])
#         left_triangle.append(l)
#         right_triangle.append(r)
#
#     return left_triangle, right_triangle
#
#
# def solution(triangle):
#     if len(triangle) == 1:
#         return triangle[0][0]
#
#     left_triangle, right_triangle = separate_triangle(triangle=triangle)
#     return max([triangle[0][0] + solution(left_triangle), triangle[0][0] + solution(right_triangle)])
#
#
# if __name__ == '__main__':
#     print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
#
# from icecream import ic
#
#
# def solution(triangle):
#     triangle.reverse()
#
#     results = [[] for _ in range(len(triangle))]
#     results[0] = [{i} for i in triangle[0]]
#
#     for row_idx, triangle_row in enumerate(triangle[1:], start=1):
#         prev_row_idx = row_idx - 1
#         l = []
#         for current_idx, triangle_item in enumerate(triangle_row):
#             l1 = set(map(lambda i: i + triangle_item, results[prev_row_idx][current_idx]))
#             l2 = set(map(lambda i: i + triangle_item, results[prev_row_idx][current_idx + 1]))
#             l.append({*l1, *l2})
#         results[row_idx] = l
#
#     return max(results[-1][0])
#
#
# if __name__ == '__main__':
#     print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
from icecream import ic


def solution(triangle):
    max_distances = [list() for _ in range(len(triangle))]
    for h in range(len(triangle) - 1, -1, -1):
        if h == len(triangle) - 1:
            max_distances[h] = triangle[h]
            continue
        for w in range(len(triangle[h])):
            max_distances[h].append(max([max_distances[h + 1][w] + triangle[h][w], max_distances[h + 1][w + 1] + triangle[h][w]]))
    return max_distances[0][0]


if __name__ == '__main__':
    print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
