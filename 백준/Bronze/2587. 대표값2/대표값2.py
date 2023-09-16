sum1 = 0
L = []
for i in range(5):
    n = int(input())
    L.append(n)
    sum1 += n
L.sort()
print(sum1//5)
print(L[2])
