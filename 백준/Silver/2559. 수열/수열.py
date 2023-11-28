n,k = [int(x) for x in input().split()]

arr=[int(x) for x in input().split()]
prefix = [0 for _ in range(n+1)] #1칸더 크게 만들기
temp = 0
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]
answer=[] 
for i in range(k,n+1):
    answer.append(prefix[i]-prefix[i-k])
print(max(answer))
