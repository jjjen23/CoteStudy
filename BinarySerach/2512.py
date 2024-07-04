# 백준 : 예산(아주 맘에드는 문제야)
n = int(input())
list_n = list(map(int, input().split()))
m = int(input()) #총예산

start = 1
end = max(list_n)
res = 0 #최종답 저장 변수

while start <= end:
    total = 0
    mid = (start+end) // 2

    for D in list_n:
        if D <= mid:
            total += D
        else:
            total += mid

    if total <= m:
        res = max(res, mid) #가능한 최고 값으로 갱신해주기
        start = mid+1
    else:
        end = mid - 1

print(res)