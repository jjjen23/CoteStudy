# 백준 : 차집합
na, nb = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

res = list(setA.difference(setB))
if len(res) == 0:
    print(0)
else:
    res.sort()
    print(len(res))
    print(' '.join(map(str, res)))
