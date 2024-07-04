# 백준 : 국영수
n = int(input())

list1 = []

for _ in range(n):
    tem = input().split()
    list1.append([tem[0], int(tem[1]), int(tem[2]), int(tem[3])])

sortedlist1 = sorted(list1, key=lambda x:(-x[1],x[2],-x[3],x[0]))

for tem in sortedlist1:
    print(tem[0])