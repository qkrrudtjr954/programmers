# hash 를 사용한 풀이 -> dict
def solution1(phone_book):
    hash_map = {phone_num: True for phone_num in phone_book}

    for phone_num in phone_book:
        # 문자의 자릿수를 하나씩 증가하며 조회
        # ex) 123456 -> 1, 12, 123, 1234, 12345
        for i in range(1, len(phone_num)):
            if hash_map.get(phone_num[:i], False):
                return False
    return True


# python 내장 함수를 사용한 풀이
def solution2(phone_book):
    phone_book.sort()

    # 문자열을 정렬하면 다음과 같이 정렬됨
    # '1', '123', '1234', '2', '21', '213', '34' ...
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True
