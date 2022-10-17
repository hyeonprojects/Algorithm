import collections
from typing import Deque


def check_palindrome(input: str) -> bool:
    strs: Deque = collections.deque()

    for char in input:
        if char.isalnum():
            strs.append(char.lower())

    while len(str) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# def longest_palindrome(check_string: str):
#     # 반복을 돌려서 글자 전체 숫자에서 역순으로 팰린드롬을 조사
#     longest_palindrome_string = ''
#     length = len(check_string)
#     while check_string:

def longest_palindrome(check_string: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(check_string) and check_string[left] == check_string[right]:
            left -= 1
            right += 1
        return check_string[left + 1:right]


    # 해당 사항 없을 떄 빠르게 리턴
    if len(check_string) < 2 or check_string == check_string[::-1]:
        return check_string

    result = ''
    # 슬라이딩 윈도우 우츠긍로 이동
    for i in range(len(check_string) - 1):
        result = max(result,
                     expand(i, i + 1),
                     expand(i, i + 2),
                     key=len)
    return result

