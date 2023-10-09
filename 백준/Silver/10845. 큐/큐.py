import sys
queue = []

n = int(input()) #주어지는 명령의 수

for i in range(n):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        _, x = command.split()
        queue.append(int(x)) #x 타입 str -> int
    elif command == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
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
    
        
        
