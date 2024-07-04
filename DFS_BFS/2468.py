# 백준 : 안전영역
from collections import deque
import copy

n = int(input())

region = [list(map(int, input().split())) for _ in range(n)]


def bfs(x,y,h,visited):
    queue = deque([(x,y)])
    visited[x][y] = 1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while queue:
        x,y= queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<n and visited[nx][ny]==0):
                if region[nx][ny] > h:
                    visited[nx][ny] = 1
                    queue.append((nx,ny))



max_height = max(max(region[i]) for i in range(n))

res = 0
# 높이 0부터 가장 높은 지형의 높이까지 반복하면서 안전한 영역을 세기
for h in range(max_height + 1):
    visited = [[0] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            if region[i][j] > h and visited[i][j] == 0:  # 물에 잠기지 않은 지역인 경우에만 탐색 시작
                bfs(i, j, h, visited)
                count+=1

    if res < count:
        res = count

print(res)