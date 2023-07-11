from typing import Any


class Queue:
    def __init__(self, *args: Any):
        self.__items: list[Any] = list(args)
        self.__size: int = len(self.__items)

    def enqueue(self, item: Any):
        self.__items.append(item)
        self.__size += 1

    def dequeue(self):
        if self.empty():
            raise IndexError("dequeue from empty queue")
        item: Any = self.__items.pop(0)
        self.__size -= 1
        return item

    def empty(self):
        return not self.__size

    def __str__(self):
        return f"{self.__items}"

    def __repr__(self):
        return f"{self.__items}"

    def __len__(self):
        return self.__size

    def __iter__(self):
        if self.empty():
            return None
        for item in self.__items:
            yield item

"""
append()와 pop(0)를 이용하면 리스트로도 만들 수 있다.
"""


# 그러나 기본 라이브러리로 큐가 구현되어 있다.
import queue

q1 = queue.Queue()

q1.put(1)
q1.put(2)
q1.get()

# deque도 있다.
# deque는 양방향에서 데이터를 추가하고 뽑을 수 있는 자료구조이다.

from collections import deque

q2 = deque([5, 6, 2])
q2.popleft()
q2.appendleft(9)

