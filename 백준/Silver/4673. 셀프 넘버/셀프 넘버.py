D = [i for i in range(1,10001)]
S = []
zi = 0
for j in range(1,10001):
    num = j
    zi = num
    for i in range(len(str(num))):
        num += zi%10
        zi = zi//10
    S.append(num)
D = list(set(D)-set(S))
D.sort()
for i in D:
    print(i)
