m = int(input())
n = int(input())
sum1 = 0
L =[]
for i in range(m,n+1):
    sum1 = 0
    for j in range(1,i+1):
        if i%j == 0:
            sum1 += 1
    if sum1 == 2:
        L.append(i)
sum1 = 0
for i in range(len(L)):
    sum1 += L[i]
if len(L) >= 1:
    print(sum1)
    print(min(L))
else:
    print(-1)
            
