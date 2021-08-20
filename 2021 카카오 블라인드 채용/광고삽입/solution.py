def convert(t: str):
    t = list(map(int, t.split(':')))
    return t[0] * 3600 + t[1] * 60 + t[2]


def convert_seconds_to_time_str(s: int):
    return '%02d:%02d:%02d' % (s / 3600, s / 60 % 60, s % 60)


def solution(play_time, adv_time, logs):
    play_time = convert(play_time)
    adv_time = convert(adv_time)

    watcher_count_in_seconds = [0] * (play_time + 1)

    for log in logs:
        s, e = log.split('-')
        watcher_count_in_seconds[convert(s)] += 1
        watcher_count_in_seconds[convert(e)] -= 1

    for i in range(1, play_time):
        watcher_count_in_seconds[i] += watcher_count_in_seconds[i - 1]

    current_watcher = sum(watcher_count_in_seconds[:adv_time])
    max_watcher = current_watcher
    max_idx = 0

    for i in range(adv_time, play_time):
        current_watcher = current_watcher + watcher_count_in_seconds[i] - watcher_count_in_seconds[i - adv_time]

        if current_watcher > max_watcher:
            max_watcher = current_watcher
            max_idx = i - adv_time + 1

    return convert_seconds_to_time_str(max_idx)

