from icecream import ic


def convert_time_str_to_int(t: str):
    t = list(map(int, t.split(':')))
    return t[0] * 3600 + t[1] * 60 + t[2]


class PlayTime:
    def __init__(self, t):
        t_str = t.split('-')
        self.start_time = convert_time_str_to_int(t_str[0])
        self.end_time = convert_time_str_to_int(t_str[1])

    @property
    def range(self):
        return self.end_time - self.start_time

    def __repr__(self):
        return f'{self.start_time} ~ {self.end_time} [{self.range}]'


def solution(play_time, adv_time, logs):
    '''
    play_time: 죠르디 동영상 재생 길이
    adv_time: 공익광고 동영상 재생 길이
    logs: 시청 정보
    return 시청자 누적 재생 시작이 가장 많은 시작시간
    '''
    p = [PlayTime(t) for t in logs]

    ic([_p for _p in p])
    answer = ''
    return answer


if __name__ == '__main__':
    solution('', '', ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
