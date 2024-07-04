# 백준 : 미로 탐색(리뷰)
from collections import deque


def bfs(n,m,maze):
    # 방문 표시 배열 만들기
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0,0)])
    visited[0][0] = 1

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    while queue:
        x,y = queue.popleft()
        # 인덱스 번호는 구하려는 값에 -1값으로 하는것 주의
        if (x==n-1 and y==m-1) :
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0<=nx<n) and (0<=ny<m) and visited[nx][ny] == 0):
                    # 문자열로 입력받았으니 문자열 1로 비교할것...! 이거 때매 계속 카운트가 안됨
                    if maze[x][y] == '1':
                        # 전꺼랑 누적 형식으로 쌓기(최단경로를 찾는 문제)
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

n, m = map(int, input().split())

# 미로 입력받기
maze = []
for _ in range(n):
    row = list(input())
    maze.append(row)

print(bfs(n,m,maze))