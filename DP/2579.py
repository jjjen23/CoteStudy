# 백준 : 계단 오르기
# 핵심은 n번째 계단에 서 있을때 관점으로 생각하는 것

n = int(input())
grade = [0]
for i in range(1, n+1):
   grade.append(int(input()))

dp = [0] * (n+1)

# 3번째 칸 까진 초기화 해주기(4번째 칸 부터 점화식 이용가능)
dp[1] = grade[1]

#n이 1일수도 있으니.. 그 경우 오류가 나지 않도록 2번 인덱스초기화는 if문 처리
if n > 1:
    dp[2] = grade[1]+grade[2] #n-1에서 n으로 올라온 경우만 존재
#dp[3] = max(grade[1]+grade[3], grade[2]+grade[3]) #n-2 ->n인 경우와 n-1 -> n인 경우중 최대값 저장

# n번째 계단에 오기 위한 경우의 수 : n-1번째 계단 이용 or n-2번째 계단 이용 중 최대 저장
# n-2 번째 계단 -> n번째 계단으로 오는 경우 : dp[n] = grade[n] + dp[n-2]
# n-1 번째 계단 -> n번째 계단으로 오는 경우 : dp[n] = grade[n] + grade[n-1] + dp[n-3]
# n-1 번째 계단 -> n번째 계단으로 오는 경우에서 dp[n-2]가 아니라 dp[n-3]을 더하는 이유는 dp[n-2]의 경우는
# 연속된 세 개의 계단을 밟는 경우가 되기 때문에 문제조건에 적합하지 않기 때문!
for i in range(3, n+1):
    dp[i] = max(grade[i]+grade[i-1]+dp[i-3], grade[i]+dp[i-2])
print(dp[n])

"""
# 런타임 에러나는 이유 : n이 1 인경우를 고려하지 않아서!
# 기존처럼 코드를 작성해줄려면 grade와 dp배열이 애초에 0으로 초기화 되어있어야 오류 안남(주석 아래 코드)
# n의 크기에 따라 동적으로 배열 크기를 할당하고 싶다면 n이 1일때의 조건을 추가하여 오류 제어하면 됨(주석 위 코드)

n = int(input())
grade = [0] * 301
for i in range(1, n+1):
   grade[i] = int(input())

dp = [0] * (301)

dp[1] = grade[1]
dp[2] = grade[1]+grade[2] # n만큼 동적으로 배열을 할당하는 경우 n이 1일 때 해당 줄에서 오류가 난다. (초기화 불가)

for i in range(3, n+1):
    dp[i] = max(grade[i]+grade[i-1]+dp[i-3], grade[i]+dp[i-2])
print(dp[n])
"""