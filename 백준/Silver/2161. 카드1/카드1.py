from collections import deque
n = int(input())
queue = deque([int(x) for x in range(1,n+1)])

while True:
    if len(queue) == 1:
        print(queue.pop())
        break
    else:
        print(queue.popleft(), end=' ')
        queue.append(queue.popleft())
