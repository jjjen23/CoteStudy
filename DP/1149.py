# 백준 : RGB거리
n = int(input())
houses = []

# 집을 칠하는 최소비용을 출력하라..
for i in range(n):
    RGB = list(map(int, input().split()))
    houses.append(RGB)

for i in range(1,n):
    # 빨간집인 경우: 이전것 중 초록 파랑 중 최소를 고르도록한다.
    houses[i][0] = min(houses[i-1][1], houses[i-1][2]) + houses[i][0]

    # 초록집인 경우 :이전것 중 빨강 파랑 중 최소를 고르도록한다.
    houses[i][1] = min(houses[i-1][0], houses[i-1][2]) + houses[i][1]

    # 파란집인 경우 :이전것 중 초록 빨강 중 최소를 고르도록한다.
    houses[i][2] = min(houses[i - 1][1], houses[i - 1][0]) + houses[i][2]
print(min(houses[n-1]))

"""
1 100 100
200 2 101
102 202 3
"""