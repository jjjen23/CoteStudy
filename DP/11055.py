# 백준 : 가장 큰 증가하는 부분 수열
n = int(input())
n_list = list(map(int, input().split()))

# 각 인덱스에는 해당 인덱스까지의 증가하는 부분수열의 최대합이 저장되어있다.
dp = n_list[:] #복사

for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j]:
            # 증가하는 조건을 만족하면 (이전시점까지 증가하는 부분 수열 합 + 현재 값 추가된 것)과 현재 상태중 더 큰 값을 저장한다.
            dp[i] = max(dp[i], dp[j] + n_list[i])

print(max(dp))