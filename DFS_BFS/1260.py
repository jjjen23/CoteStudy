# 백준 : DFS와 BFS
from collections import deque

# 정점의 개수, 간선의 갯, 탐색 시작 정점의 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# 간선의 정보 입력(양방향 그래프)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

# DFS 정의
def dfs(graph, v, visited):
    # 방문 노드 표시
    visited[v] = True
    print(v, end=' ')
    # 인접 노드 중 방문하지 않은 노드를 재귀적으로 탐색
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

# BFS 정의
def bfs(graph, start, visited):
    # 큐에 넣기
    queue = deque([start])
    # 방문 처리
    visited[start] = True
    # 큐가 빌 때 까지 하나씩 꺼내, 인접노트 방분
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)