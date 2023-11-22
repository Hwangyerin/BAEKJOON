import sys
stack = []
ans = "yes"
while True:
    stack = []
    text = sys.stdin.readline().rstrip()
    if text == ".":
        break
    for i in text:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")" or i == "]":
            if len(stack) == 0:
                ans = "no1"
                break
            else:
                if (i == ")" and stack[-1] != "(") or\
                   (i == "]" and stack[-1] != "["):
                    ans = "no1"
                else:
                    stack.pop()
        #print(stack)
    if len(stack) != 0 or ans == "no1":
        ans = "no"
    else:
        ans = "yes"
    print(ans)