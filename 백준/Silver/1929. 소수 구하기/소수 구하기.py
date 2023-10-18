def prime(p):
    for i in range(2,int(p**0.5)+1):
        if p%i==0:
            return False
    return True
m,n = [int(x) for x in input().split()]
for i in range(m,n+1):
    if prime(i) == True and i != 1:
        print(i)
