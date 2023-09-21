import sys

n = int(sys.stdin.readline().rstrip())
L =[0]*10001

for i in range(n):
    L[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    if L[i] != 0:
        for j in range(L[i]):
            print(i)
