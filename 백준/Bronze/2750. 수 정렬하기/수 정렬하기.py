L = []
n = int(input())
for i in range(n):
    L.append(int(input()))
L.sort()

for i in range(n):
    print(L[i])
