import sys
from collections import deque
n = int(input())
L = deque()
for i in range(n):
    command = [int(x) for x in sys.stdin.readline().split()]
    lenL = len(L)
    if command[0] == 1:
        L.appendleft(command[-1])
    elif command[0] == 2:
        L.append(command[-1])
    elif command[0] == 3 :
        print(L.popleft() if lenL else -1)
    elif command[0] == 4:
        print(L.pop() if lenL else -1)
    elif command[0] == 5:
        print(lenL)
    elif command[0] == 6:
        print(0 if lenL else 1)
    elif command[0] == 7:
        print(L[0] if lenL else -1)
    elif command[0] == 8:
        print(L[-1] if lenL else -1)
        
