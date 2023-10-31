n = int(input())

L = [int(x) for x in input().split()]
cnt = 0
temp = 0
for i in L:
    if i == temp:
        cnt+=1
        if temp==2:
            temp=0
        else:
            temp += 1
    else:
        continue
print(cnt)
        
