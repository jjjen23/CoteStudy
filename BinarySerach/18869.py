# 백준: 멀티버스2
from collections import defaultdict

# 0을 기본으로 하는 딕셔너리 생성하기(딕셔너리 키가 없을땐 기본값인 0 출력됨)
my_defaultdict = defaultdict(int)

n, m = map(int, input().split())

for _ in range(n):
   # 우주 리스트 입력받기
   space = list(map(int, input().split()))

   sortedspace = sorted(list(set(space)))

   # 정렬된 리스트의 값 : 인덱스(순위)를 사전에 정의
   rankdict = {}
   for i in range(len(sortedspace)):
       rankdict[sortedspace[i]] = i

   # 사전을 이용해 입력받은 기존 리스트(space) 순위 결정하기
   vector = []
   for i in space:
       vector.append(rankdict[i])

   #리스트의 순서 조합을 튜플형태로 변경하여 키로 사용할 것임 (키는 변동 불가능한 튜플 형태만 가능)
   my_defaultdict[tuple(vector)] += 1 #같은 순서쌍 등장시 카운트


res = 0
# 우주 쌍 구하기 조합 이용하면 됨 (nC2)
for i in my_defaultdict.values():
    res += (i*(i-1)) // 2
print(res)