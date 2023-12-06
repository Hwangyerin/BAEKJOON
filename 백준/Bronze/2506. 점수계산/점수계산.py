import sys
input=sys.stdin.readline

n = int(input())
L = [int(x) for x in input().split()]
sum1 = 0
cnt = 1
for i in L:
    if i == 1:
       sum1 += cnt
       cnt += 1
    elif i == 0:
        cnt = 1
print(sum1)
