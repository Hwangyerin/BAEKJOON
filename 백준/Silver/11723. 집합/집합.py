import sys
S=set()
n = int(sys.stdin.readline())
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0] == 'all':
        S = set([j for j in range(1,21)])
    elif cmd[0] == 'empty':
        S = set()
    if len(cmd) == 2:
        cmd, x = cmd[0], int(cmd[1])
    if cmd == 'add':
        S.add(x)
    elif cmd == 'remove':
        S.discard(x)
    elif cmd == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd == 'toggle':
        if x in S:
            S.discard(x)
        else:
            S.add(x)
    
        
