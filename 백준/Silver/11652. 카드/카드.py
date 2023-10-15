import sys
n = int(input())
numD = {}
L = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num in numD:
        numD[num] += 1
    else:
        numD[num] = 1
maxNum = max(numD.values())
for k in numD.keys():
    if numD[k] == maxNum:
        L.append(k)
L.sort()
print(L[0])
