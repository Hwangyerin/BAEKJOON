n = int(input())
ans = "YES"
for i in range(n):
    stack = []
    text = input()
    for j in text:
        if j =="(":
            stack.append(j)
        elif j == ")":
            if len(stack) == 0:
                ans = "NO"
                break
            else:
                stack.pop()
                if j == ")" and stack.pop != "(":
                    ans = "NO"
        if len(stack) != 0:
            ans = "NO"
        else:
            ans = "YES"
    print(ans)