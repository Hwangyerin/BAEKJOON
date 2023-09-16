n = int(input())
L = []
for i in range(n):
    m = [int(x) for x in input().split()]
    L.append(m)

L.sort(key=lambda x: (x[1], x[0]))

for i in L:
    print(i[0],i[1])
