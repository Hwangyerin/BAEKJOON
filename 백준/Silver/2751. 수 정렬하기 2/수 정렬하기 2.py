import sys
num= []
n = int(input())
for i in range(n):
    num.append(int(sys.stdin.readline().rstrip()))

num.sort()
for i in range(n):
    print(num[i])
