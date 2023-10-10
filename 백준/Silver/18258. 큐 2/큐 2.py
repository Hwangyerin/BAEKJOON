from collections import deque
import sys

n = int(input())
queue = deque([])

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        _, x = command.split()
        queue.append(int(x))
    elif command == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
