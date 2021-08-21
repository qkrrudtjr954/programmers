from bisect import bisect_left


def solution(info, query):
    idx_map = {
        '-': 0,
        'cpp': 1, 'java': 2, 'python': 3,
        'backend': 1, 'frontend': 2,
        'junior': 1, 'senior': 2,
        'chicken': 1, 'pizza': 2
    }

    score_list = [[] for _ in range(4 * 3 * 3 * 3)]

    for info_str in info:
        info_str = info_str.split()
        index = (
            idx_map[info_str[0]] * 3 * 3 * 3,  # 언어
            idx_map[info_str[1]] * 3 * 3,  # 직군
            idx_map[info_str[2]] * 3,  # 경력
            idx_map[info_str[3]],  # 소울푸드
        )
        score = int(info_str[4])  # score

        for i in range(1 << 4):
            idx = 0
            for j in range(4):
                if i & (1 << j):
                    idx += index[j]

            score_list[idx].append(score)

    answer = []

    for i in range(4 * 3 * 3 * 3):
        score_list[i].sort()

    for query_str in query:
        query_str = query_str.split()
        index = idx_map[query_str[0]] * 3 * 3 * 3 + idx_map[query_str[2]] * 3 * 3 + idx_map[query_str[4]] * 3 + idx_map[query_str[6]]
        score = int(query_str[7])

        count = len(score_list[index]) - bisect_left(score_list[index], score)

        answer.append(count)

    return answer


if __name__ == '__main__':
    assert solution([
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ], [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]) == [1, 1, 1, 1, 2, 4]
