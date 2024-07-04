# 백준 : 숨바꼭질
from collections import deque
n, k = map(int, input().split())
dist = [0]*100001

def bfs(dist, n, k):
        queue = deque([n])

        while queue:
            n = queue.popleft()
            if n == k:
                return dist[n]
            for nx in [n-1, n+1, n*2]:
                if 0 <= nx <= 100000 and not dist[nx]:
                    queue.append(nx)
                    dist[nx] += dist[n]+1


# bfs로 탐색 경우의 수 3가지를 탐색한다. 단, 매번 위치가 0과 100,000 사이인지 검사할 것
print(bfs(dist, n, k))