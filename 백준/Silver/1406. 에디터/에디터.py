import sys
text1 = list(sys.stdin.readline().rstrip()) #초기에 편집기에 입력되어 있는 문자열
text2 = [] 
n = int(sys.stdin.readline()) #입력할 명령어의 개수
for i in range(n):
    cmd = list(sys.stdin.readline().split())
    if cmd[0] == "L":
        if text1:
            text2.append(text1.pop())
    elif cmd[0] == "D":
        if text2:
            text1.append(text2.pop())
    elif cmd[0] == "B":
        if text1:
            text1.pop()
    elif cmd[0] == "P":
        text1.append(cmd[1])
text1.extend(reversed(text2))
print(''.join(text1))
