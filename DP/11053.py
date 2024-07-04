# 백준 : 가장 긴 증가하는 부분 수열
n = int(input())
list_n = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if list_n[i] > list_n[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))