# 백준 : 과자 나눠주기
m, n = map(int, input().split())
height = list(map(int, input().split()))

start = 1 #최소 막대과자의 길이는 1일것 0으로 설정하니까 ZeroDivisionError남 ㅡㅡ
end = max(height)
res = 0

while start <= end:
  cnt = 0
  mid = (start + end) // 2

  for H in height:
      cnt += H//mid #몫을 구하는 연산자로 쉽게 해결 가능..!

  # 최대 길이까지 이진탐색
  if cnt >= m:
      res = max(res, mid)
      start = mid + 1
  else:
      end = mid - 1

print(res)

