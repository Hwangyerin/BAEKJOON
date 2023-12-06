import sys
input=sys.stdin.readline
test = int(input()) #test case
for i in range(test):
    s = int(input())
    n = int(input())
    for i in range(n):
        q,p=map(int, input().split())
        s += (q*p)
    print(s)
