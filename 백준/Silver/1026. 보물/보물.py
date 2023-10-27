n = int(input())
hap = 0
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
A.sort()
B.sort(reverse=True)
for i in range(n):
    hap+=A[i]*B[i]
print(hap)
