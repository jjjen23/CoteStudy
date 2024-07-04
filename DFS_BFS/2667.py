# 백준 : 단지번호붙이기
"""
# dfs
def dfs(x,y):
    global count

    dx = [0,0,-1,1]
    dy = [1,-1,0,0]

    visited[x][y] = True
    if apt[x][y] == '1':
        count += 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if (0<=nx<n and 0<=ny<n and apt[nx][ny] == '1' and visited[nx][ny] == False):
            dfs(nx,ny)

n = int(input())

apt = []
for _ in range(n):
    row = list(input())
    apt.append(row)

res = [] #결과를 저장할 배열 생성
visited = [[False]*n for _ in range(n)]

count = 0
res = []

# 그래프에서 1발견시 dfs호출
for i in range(n):
    for j in range(n):
        if apt[i][j] == '1' and visited[i][j] == False:
            dfs(i,j) # 하나의 재귀적 dfs호출이 끝나면
            res.append(count) #각 dfs 카운트 저장
            count = 0 # 다음 dfs를 위해 0으로 초기화

 #오름차순 정렬 및 출력
res.sort()
print(len(res))
for i in res:
    print(i)

"""
#bfs
from collections import deque

def bfs(x,y):
    global count
    queue = deque([(x,y)])
    apt[x][y] = '0'
    count += 1

    while queue:
        x,y = queue.popleft()

        dx = [0,0,-1,1]
        dy = [1,-1,0,0]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if (0<=nx<n and 0<=ny<n and apt[nx][ny] == '1'):
                count += 1
                apt[nx][ny] = '0' # bfs 탐색된것은 0으로 변경해주기!
                queue.append((nx,ny))
    return count


n = int(input())

apt = []
for _ in range(n):
    row = list(input())
    apt.append(row)

res = [] #결과를 저장할 배열 생성
visited = [[False]*n for _ in range(n)]

count = 0
res = []

# 그래프에서 1발견시 dfs호출
for i in range(n):
    for j in range(n):
        if apt[i][j] == '1':
            bfs(i,j) # 하나의 bfs호출이 끝나면
            res.append(count) #각 bfs 카운트 리스트에 저장
            count = 0 # 다음 bfs를 위해 count변수 0으로 초기화

 #오름차순 정렬 및 출력
res.sort()
print(len(res))
for i in res:
    print(i)