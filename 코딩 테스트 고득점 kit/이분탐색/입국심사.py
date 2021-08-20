import copy


def solution_v1(n, times):
    times.sort()
    waiting_time = copy.copy(times)
    answer = 0

    while n != 0:
        t = min(waiting_time)
        waiting_time = list(map(lambda wt: wt - t if wt - t >= 0 else 0, waiting_time))
        answer += t
        idx = next(idx for idx, t in enumerate(waiting_time) if t == 0)
        waiting_time[idx] += times[idx]
        n -= 1

    return answer


# 컷닝했씁니다. 🙏
def solution(n, times):
    times.sort()

    min_time = 1
    max_time = times[-1] * n

    answer = max_time

    while min_time <= max_time:
        mid_time = int((min_time + max_time) / 2)

        s = sum(int(mid_time / time) for time in times)

        if s >= n:
            if answer > mid_time:
                answer = mid_time
            max_time = mid_time - 1
        else:
            min_time = mid_time + 1
    return answer


if __name__ == '__main__':
    print(solution_v1(6, [7, 10]))
    print(solution(6, [7, 10]))
