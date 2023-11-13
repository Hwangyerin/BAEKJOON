n= int(input())
L=[int(x) for x in input().split()]
L=list(set(L))
L.sort()
for i in L:
    print(i,end=' ')
