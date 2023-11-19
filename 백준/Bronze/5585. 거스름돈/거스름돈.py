change = [500,100,50,10,5,1]
cnt = 0
n=int(input())
n = 1000-n
while n>0:
    for i in change:
        cnt=cnt+(n//i)
        n = n%i
print(cnt)
