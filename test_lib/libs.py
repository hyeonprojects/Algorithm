
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
#