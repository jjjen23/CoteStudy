# 백준 : 촌수계산
from collections import deque

n = int(input()) # 전체 사람 수
x, y = map(int, input().split()) # 계산해야 하는 두 사람의 번호
m = int(input()) # 부모자식 간의 관계 수

# 관계 그래프 정의(양방향)
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,visited,start,end):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        # 촌수가 존재 한다면 촌수 반환
        if v == end:
            return visited[v]
        for vn in graph[v]:
            if not visited[vn]:
                visited[vn] += visited[v] + 1
                queue.append(vn)
    # 촌수가 없다면 -1 반환
    return -1

print(bfs(graph,visited,x,y))
# 나 천재아니묘?? ㅇㅈㄹ