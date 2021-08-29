from icecream import ic


def get_record(row):
    if row.startswith('Leave'):
        action, uid = row.split()
        nickname = None
    else:
        action, uid, nickname = row.split()

    return action, uid, nickname


def solution(record):
    nickname_db = {}

    for action, uid, nickname in map(get_record, record):
        if action in ['Enter', 'Change']:
            nickname_db[uid] = nickname

    answer = []
    for action, uid, nickname in map(get_record, record):
        if action == 'Enter':
            answer.append(f'{nickname_db[uid]}님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(f'{nickname_db[uid]}님이 나갔습니다.')

    return answer


if __name__ == '__main__':
    ic(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
