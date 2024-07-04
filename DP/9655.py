# 백준 : 돌 게임
n = int(input())

# n이 홀수면 상근이가 이기고 짝수면 창영이가 이긴다.
if n % 2 == 0:
    print('CY')
else:
    print('SK')
