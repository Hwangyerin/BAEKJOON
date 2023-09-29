import sys

n = int(input())
L = []

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        L.append(com[1])
    elif com[0] == 'pop':
        if len(L) > 0:
            print(L.pop(-1))
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(L))
    elif com[0] == 'empty':
        if len(L) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if len(L) > 0:
            print(L[-1])
        else:
            print(-1)
