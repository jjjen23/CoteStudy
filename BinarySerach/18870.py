# 백준 : 좌표압축
n = int(input())
list_n = list(map(int,input().split()))

set_n = list(set(list_n))
set_n.sort() # 집합으로 만든 뒤 정렬하기(중복원소을 제외하고 원소당 하나의 인덱스 번호를 결정하기 위해)
#print(set_n)

# 사전에 key는 원소 value는 해당 원소 인덱스 번호로 저장
my_dict = {}
for i in range(len(set_n)):
    my_dict[set_n[i]] = i
#print(my_dict)

# 기존에 입력 받은 리스트 원소를 키를 기준으로 값 출력(정답)
res = [] #정답을 저장할 리스트
for i in range(n):
    res.append(my_dict[list_n[i]])
print(' '.join(map(str,res)))