
# DFS 깊이 우선 탐색
# 한 가지 정점과 연결된 모든 정점을 탐색해야하는 경우
# 경로를 찾아야 되는 경우
# 사이클이 존재하는 경로 찾는 경우
# 스택 또는 재귀함수로 구현

class Graph:
    def __init__(self):
        self.v = 0
        self.adj = []

    def DFS(self, visited: list[bool]):
        # 현재 노드를 방문한 것으로 표시하고 값을 출력
        visited[self.v] = True
        




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