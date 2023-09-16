import sys
n = int(input())
L = list(map(int, sys.stdin.readline().rstrip().split()))
S = list(set(L))
S.sort()

D = {S[i] : i for i in range(len(S))}
for i in L:
    print(D[i], end=' ')