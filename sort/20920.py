# 백준 : 영단어 암기는 괴로워
from collections import defaultdict
n, m = map(int, input().split())

dict1 = defaultdict(int) # 0으로 초기화

for _ in range(n):
 tem = input()
 if len(tem) >= m:
    dict1[tem] += 1

# 우선순위가 여러개 적용되는 경우 다음과 같이 한다. (내림차순 조건의 경우 - 만 붙이면 해결됨!)
sortedlist = sorted(dict1.items(), key=lambda x : (-x[1],-len(x[0]),x[0]))

for x in sortedlist:
    print(x[0])


"""
# 힙을 이용한 정렬
from collections import defaultdict
import heapq

n, m = map(int, input().split())

dict1 = defaultdict(int) # 0으로 초기화
heap = []

for _ in range(n):
 tem = input()
 if len(tem) >=m:
   dict1[tem] += 1

# 튜플 형태로 딕셔너리에서 하나씩 꺼내기
for word, freq in dict1.items():
    heapq.heappush(heap, (-freq, -len(word), word))

while heap:
    res = heapq.heappop(heap)
    print(res[2])
"""