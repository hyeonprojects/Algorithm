"""
Lib Application =
"""
import collections
import re


# 문자열 뒤집기 시리즈
def reverse_string1(string_data: str) -> str:
    """
    문자열 순서 뒤집기 slice로 뒤집기
    :param string_data: 뒤집을 문자열
    :return: 반전된 문자열
    """
    return string_data[::-1]


def reverse_string2(string_data: str) -> str:
    """
    문자열 순서 뒤집기 reversed 함수 사용
    :param string_data: 뒤집을 문자열
    :return: 반전된 문자열
    """
    return "".join(reversed(string_data))


def reverse_string3(string_data: str) -> str:
    """
    문자열 순서 뒤집기, 가장 단순한 반복문 방법
    :param string_data: 뒤집을 문자열
    :return: 반전된 문자열
    """
    reversed_str = ""
    for i in string_data:
        reversed_str = i + reversed_str
    return reversed_str


def isPalindrome(string_data: str) -> bool:
    """
    팰린드롬 : 앞 뒤가 바뀌어도 똑같은 문자인지 확인하는 방법
    :param string_data: 팰린드롬 체크할 문자열 데이터
    :return: true인 경우는 팰린드롬이며 false인경우 아님
    """
    string_data = string_data.lower()
    # 불필요한 문자
    string_data = re.sub()


def most_common_word(paragraph: str, banned: list[str] | None) -> str:
    """
    금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력함
    대소문자를 구별하지 않고, 구두점(마침표, 쉼표 등) 무시함
    :param paragraph: 조회할 문자열
    :param banned: 제외할 문자열
    :return: 금지된 단어를 제외할 제일 빈도수 높은 문자열
    """
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


def group_anagrams(string_datas: list[str]) -> list[list[str]]:
    """
    문자열 배열을 받아서 애너그램 단위로 그루핑 하는 함수
    :param string_datas: 문자열 배열
    :return: 리스트 안에 리스트단위로 애너그램 단위의 그루핑 합니다.
    """
    anagrams = collections.defaultdict(list)

    for word in string_datas:
        anagrams["".join(sorted(word))].append(word)
    return list(anagrams.values())


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(most_common_word(paragraph, banned))

    data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(data))
