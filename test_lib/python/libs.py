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


def is_palindrome(string_data: str) -> bool:
    """
    팰린드롬 : 앞 뒤가 바뀌어도 똑같은 문자인지 확인하는 방법
    :param string_data: 팰린드롬 체크할 문자열 데이터
    :return: true인 경우는 팰린드롬이며 false인경우 아님
    """
    left, right = 0, len(string_data) - 1
    
    while left < right:
        # 왼쪽 포인터가 가리키는 문자가 유효하지 않으면 오른쪽으로 이동
        while left < right and not string_data[left].isalnum():
            left += 1
        # 오른쪽 포인터가 가리키는 문자가 유효하지 않으면 왼쪽으로 이동
        while left < right and not string_data[right].isalnum():
            right -= 1
        
        # 두 포인터가 가리키는 문자를 비교
        if string_data[left].lower() != string_data[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


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


def binary_search(arr: list, val):
    """
    비 재귀적 이진 탐색, 찾는 데이터가 arr에 있나??
    :param arr:
    :param val:
    :return:
    """
    first, last = 0, len(arr) - 1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            last = mide - 1
        else:
            first = mide + 1
    return -1


def dfs(graph: Dict, start: int):
    """
    깊이 우선 탐색 DFS
    핵심은 필요한 노드의 데이터가 발견되었을떄 뺴내거나 또는 이를 사용해서 개발
    :param graph: Dict 자료형 형태로 준다. key는 노드 value는 인접노드
    :param start:
    :return: 
    """
    visited = {i: False for i in graph.keys()}

    def search(current: int):
        visited[current] = True
        for nxt in graph[current]:
            if not visited[nxt]:
                search(nxt)

    search(start)


def dfs_stack(start_node):
    """
    알고리즘 분석을 위한 용도
    dfs의 알고리즘 구현 방법에 대해서 논의함.
    """
    # 1) stack 에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]

    while True:
        # 2) stack이 비어있는지 확인
        if len(stack) == 0:
            print('All node searched.')
        return None

        # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()

        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
        return node

        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        stack.extend(children)

        # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복


class Stack:
    """
    Stack 자료구조를 사용할 수 있도록 클래스로 개발
    """
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):

        return self.items.pop()

    def peek(self):
        """
        최근에 넣은 데이터를 빼지 않고 알고 싶을떄
        """
        return self.items[-1]

    def is_empty(self):
        return not self.items





# if __name__ == '__main__':
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    # banned = ["hit"]
    # print(most_common_word(paragraph, banned))
    #
    # data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # print(group_anagrams(data))
