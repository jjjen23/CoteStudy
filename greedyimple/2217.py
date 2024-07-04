# 백준 : 로프(그리디)
n = int(input())

w_list = []
for _ in range(n):
    tem = int(input())
    w_list.append(tem)

sortedlist = sorted(w_list, reverse=True)

res = []
for i in range(n):
    res.append(sortedlist[i] * (i+1))
print(max(res))


