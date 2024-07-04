# 백준 : 로봇청소기
from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())

# 인덱스 번호에 따라 북(0) -> 동(1) -> 남(2) -> 서(3) 시계방향순
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0]*m for _ in range(n)] # 청소 유무 표시

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

cnt = 0

def bfs(x,y,d):
    global cnt
    queue = deque([(x,y)])
    # 현재칸이 청소되지 않은 경우, 현재 칸을 청소한다.
    visited[x][y] = 1
    cnt += 1

    while queue:
         x, y = queue.popleft()
         flag = 0

         for _ in range(4):
             d = (d+3) % 4 #반시계 방향으로 돌려돌려 돌림판
             nx = x + dx[d]
             ny = y + dy[d]

             # 3.현재칸 주변 4칸 중 아직 청소되지 않았고,빈칸인 경우 현재 칸을 청소한다.
             if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                if visited[nx][ny] == 0:
                 visited[nx][ny] = 1
                 queue.append((nx, ny))
                 cnt += 1
                 flag = 1 #반시계 방향으로 돌아갔을 때 빈칸이 있다는 것을 의미
                 break #해당칸기준으로 상하좌우 탐색 종료 -> 다시 1번으로 돌아감

        # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우(flag가 0인경우)
         if flag == 0:
             # 2-1. 방향 유지하고 한칸 후진가능한 경우(후진한 좌표가 벽이 아닌경우)
             if graph[x-dx[d]][y-dy[d]] != 1:
                 # x,y좌표는 튜플형태로 추가하는거 잊지말자!!!
                 queue.append((x-dx[d], y-dy[d])) #해당 좌표를 큐에 추가(1번으로 돌아감)
             # 2-2. 방향 유지하고 후진 불가능 한경우 종료(종료 조건에 해당)
             else:
                 return cnt #완전종료조건에 해당


print(bfs(r,c,d))