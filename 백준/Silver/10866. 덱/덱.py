import sys
n = int(input())
deque = []

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if 'push_front' in command:
        _, x = command.split()
        if len(deque) != 0:
            deque.insert(0,x)
        else:
            deque = [x]
    if 'push_back' in command:
        _, x = command.split()
        deque.append(x)
    elif command == 'pop_front':
        if len(deque) != 0:
            print(deque.pop(0))
        else:
            print(-1)
    elif command == 'pop_back':
        if len(deque) != 0:
            print(deque.pop(-1))
        else:
            print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if len(deque) != 0:
            print(deque[0])
        else:
            print(-1)
    elif command == 'back':
        if len(deque) != 0:
            print(deque[-1])
        else:
            print(-1)
    
        
        
