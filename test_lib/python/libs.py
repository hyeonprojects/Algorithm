
# DFS 깊이 우선 탐색
# 한 가지 정점과 연결된 모든 정점을 탐색해야하는 경우
# 경로를 찾아야 되는 경우
# 사이클이 존재하는 경로 찾는 경우
# 스택 또는 재귀함수로 구현

visited = [False] * 9

graph = [
    [],
    [2, 3, 8],
    [1]
]

# 핵심은 방문이 있는지에 대한 데이터 값이 있고, 이를 node간에 연결된 edge를 적혀있어야함.

def DFS(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')

    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i , visited)


# 다른 구현

from collections import deque

# set 중복은 허용하지 않는다. 순서가 없다. set 자료구조
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1

def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited


# 해시테이블
# key와 value가 있는 값이니

def create_hashtable(keys: list[str], values: list[str]) -> dict:
    """
    해쉬테이블 만들어주기 갯수가 동일해야함
    """
    hash_table = {}
    for key, value in zip(keys, values):
        hash_table[key] = value
        print(hash_table[key].items)
    return hash_table


# 문제에서 선입 선출, 후입 선출의 단서가 보이면 사용

if __name__ == '__main__':
    print(BFS_with_adj_list(graph_list, root_node))
    print(BFS_with_adj_list(graph_list, root_node))
