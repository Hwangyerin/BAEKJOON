n = int(input())
num_list = map(int, input().split())
cnt = 0
sum1 = 0
for i in num_list:
    cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            cnt += 1
    if cnt == 2:
        sum1 += 1
print(sum1)
