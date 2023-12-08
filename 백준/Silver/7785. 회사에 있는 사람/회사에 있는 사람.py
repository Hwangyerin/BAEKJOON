import sys
input = sys.stdin.readline
n= int(input())
L = set()
for i in range(n):
    name, condition = map(str, input().split())
    if condition == 'enter':
        L.add(name)
    else:
        L.remove(name)
L = list(L)
L.sort(reverse=True)
for _ in L:
    print(_)
