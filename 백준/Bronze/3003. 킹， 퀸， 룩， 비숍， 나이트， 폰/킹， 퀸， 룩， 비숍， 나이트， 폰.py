chess = [1,1,2,2,2,8]
my_chess = [int(x) for x in input().split()]
L =[]
for i in range(len(chess)):
    L.append(chess[i]-my_chess[i])
for i in range(len(L)):
    print(L[i], end=' ')
