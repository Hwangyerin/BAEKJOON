import sys
imput = sys.stdin.readline
N, L = map(int,input().split())
H = [int(x) for x in input().split()]
H.sort()
for j in range(N):
    if L >= H[j]:
        L+=1
    else:
        break
print(L)
