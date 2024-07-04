# 백준 : 아 저는 볶음밥이요 (구현)

D = int(input())
N, M, K = map(int,input().split())

total_mandoo = []
mixed_rice = []

A = D - N%D
B = D - M%D

# 1. 볶음밥 안뺏긴 경우 군만두 서비스 개수, 볶음밥 수 저장
total_mandoo.append(N//D + M//D + K//D)
mixed_rice.append(K)

# 2. 짜장면에게 볶음밥 뺏겼을때 군만두 서비스 개수, 볶음밥 수 저장
total_mandoo.append((N+A)//D + M//D + (K-A)//D)
mixed_rice.append(K-A)

# 3. 짬뽕에게 볶음밥 뺏겼을때 군만두 서비스 개수, 볶음밥 수 저장
total_mandoo.append(N//D + (M+B)//D + (K-B)//D)
mixed_rice.append(K-B)

# 4. 짜장면, 짬뽕에게 볶음밥 뺏겼을때 군만두 서비스 개수, 볶음밥 수 저장
total_mandoo.append((N+A)//D + (M+B)//D + (K-A-B)//D)
mixed_rice.append(K-A-B)

# [(만두수,볶음밥수), (만두수,볶음밥수) .. ] 이런식으로 튜블로 묶어 리스트 재배열
ZIP = list(zip(total_mandoo, mixed_rice))
# 정렬조건 : 1. 군만두 최대이면서 2. 볶음밥 최대인것 순으로 정렬
ZIP.sort(key = lambda x:(-x[0],-x[1]))
print(ZIP[0][1])