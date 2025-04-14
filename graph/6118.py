import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) #1억

# 숨바꼭질
# 재석이의 발냄새를 최대한 숨길 수 있는 헛간을 찾아라 = 가장 멀리 있는
# n = 헛간의 개수, 모든 헛간은 m개의 양방향 길로 이어짐
# 1번 헛간에서의 거리가 멀어질수록 감소한다 -> 1번헛간 기준 다익스트라
# 숨어야하는 헛간 번호를, 헛간까지의 거리를, 헛간과 같은 거리에 있는 헛간의 개수 출력
n, m = map(int, input().split())

# 노드개수만큼
graph = [[] for i in range(n+1)]
# 최단거리테이블 모두 무한으로 초기화
distance = [INF]*(n+1)

# 간선정보 입력받기
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q,(cost,i))

dijkstra(1)

a1 = 0
a2 = 0
for i in range(1,len(distance)):
    if distance[i] > a2:
        a1 = i
        a2 = distance[i]
a3 = distance.count(a2)

print(a1, a2, a3)


