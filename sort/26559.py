# 백준 : Friends

n = int(input())

for i in range(n):
    m = int(input())
    dict1 = {}
    for i in range(m):
        name, val = input().split()
        val = int(val)
        dict1[val] = name
    # x[0] 기준으로 정렬됨 그니까 lambda 없을땐 default가 첫번째이므로, key 기준으로 정렬됨
    dict2 = dict(sorted(dict1.items(), reverse=True))
    print(', '.join(map(str, dict2.values())))
