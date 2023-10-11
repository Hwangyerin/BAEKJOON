n = int(input())
num_list = map(int, input().split())
answer = 0
for j in num_list:
    L = []
    for i in range(1,int(j**0.5)+1):
        if j%i == 0:
            L += [i,j//i]
    if len(set(L)) == 2:
        answer += 1
print(answer)