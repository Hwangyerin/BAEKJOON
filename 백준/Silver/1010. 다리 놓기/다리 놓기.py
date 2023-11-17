def factorial(a):
    num = 1
    for i in range(1,a+1):
        num*=i
    return num

case=int(input())
for i in range(case):
    n,m=[int(x) for x in input().split()]
    answer = factorial(m)//(factorial(n)*factorial(m-n))
    print(answer)

