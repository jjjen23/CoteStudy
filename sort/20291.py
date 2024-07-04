# 백준 : 파일정리
from collections import defaultdict

n = int(input())
dict1 = defaultdict(int)

for _ in range(n):
    name, ex = input().split(".")
    dict1[ex] += 1

sortedlist = sorted(dict1.items(), key=lambda x : x[0])

for res in sortedlist:
    # print(res[0], res[1])
    print(f'{res[0]} {res[1]}')