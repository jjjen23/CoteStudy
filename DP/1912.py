# 백준 : 연속합
n = int(input())
list_n = list(map(int, input().split()))

for i in range(1,n):
    list_n[i] = max(list_n[i], (list_n[i]+list_n[i-1]))

print(max(list_n))