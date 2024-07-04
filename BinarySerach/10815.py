# 백준 : 숫자 카드
n = int(input())
card = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

card.sort()# 이진탐색은 정렬 필수!!

def binary_search(arr, target):
    start, end = 0, len(arr)-1 #인덱스 첫, 끝 번호
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1 #찾으면 1 반환
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0 #찾을 수 없다면 0 반환

res = []

for i in list_m:
    tem = binary_search(card, i)
    res.append(tem)

print(' '.join(map(str, res)))