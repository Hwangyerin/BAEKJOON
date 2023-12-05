import sys
L=[]
input = sys.stdin.readline
N=int(input())
for _ in range(N):
    L.append(int(input()))
for i in sorted(L):
    print(i)