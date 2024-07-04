# 백준 : 스타트링크(논의...)
from collections import deque
f, s, g, u, d = map(int, input().split())

dist = [0] * (f + 1)

# 방문 여부를 기록하는 visited배열과 이동 최소 횟수를 기록하는 dist배열을 따로 만들어야함
def bfs(s,g):
    queue = deque([s])

    while queue:
        v = queue.popleft()
        dist[s] = 1

        if v == g:
            return dist[v]-1

        for nv in [v-d, v+u]:
            # f층까지 범위에 포함해줘야 합니다(당연함 도달해야함)

            if 0 < nv <= f and dist[nv] == 0:
                dist[nv] = dist[v] + 1
                queue.append(nv)

    return "use the stairs"

print(bfs(s,g))

# 시작점은 포함되면 안된다가 관건 같은디..리얼 모르겟따.

"""
# 백준 : 스타트링크
from collections import deque
f, s, g, u, d = map(int, input().split())

dist = [0] * (f + 1)

# 방문 여부를 기록하는 visited배열과 이동 최소 횟수를 기록하는 dist배열을 따로 만들어야함
def bfs(s,g):
    queue = deque([s])

    while queue:
        v = queue.popleft()

        if v == g:
            return dist[v]

        for nv in [v-d, v+u]:
            # f층까지 범위에 포함해줘야 합니다(당연함 도달해야함)
            if 0 < nv <= f and dist[nv] == 0:
                dist[nv] = dist[v] + 1
                queue.append(nv)

    return "use the stairs"

print(bfs(s,g))
"""