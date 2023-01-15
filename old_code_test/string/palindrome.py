import collections
from typing import Deque


def is_palindrome(input: str) -> bool:
    strs = []
    for char in input:
        if char.isalnum(): # isalnum은 영문자와 숫자만 판별한다.
            strs.append(char.lower()) # lower는 소문자로 바꿔준다.
    
    # 판별 여부
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def is_palindrome2(input: str) -> bool:

    strs: Deque = collections.deque()

    for char in input:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True

if __name__ == '__main__':
    # input_data = input("영어로된 팰린드롬을 체크하고 싶은 문장을 적어주세요 : ")
    # print(is_palindrome(input_data))

    input_data1 = 'A man, a plan, a canal: Panama'
    input_data2 = 'race a car'

    print(is_palindrome2(input_data1))
    print(is_palindrome2(input_data2))


