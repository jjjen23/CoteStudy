# 백준 : 바이러스
from collections import deque
# 컴퓨터 수
N = int(input());
# 간선 수
E = int(input());

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

# 양방향 간선 추가하기
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b);
    graph[b].append(a);

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
          if not visited[i]:
              queue.append(i)
              visited[i] = True


bfs(graph, 1, visited)
print(visited.count(True)-1) #자기 자신은 제외하고 카운트 한다.

