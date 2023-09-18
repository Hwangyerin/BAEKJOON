
while True:
    L =[]
    sum1 = 0
    num = int(input())
    if num == -1:
        break
    else:
        for j in range(1,num):
            if num%j == 0:
                sum1+=j
                L.append(j)
        if sum1 == num:
            print(num, end=' = ')
            print(*L,sep=' + ')
        else:
            print(num,'is NOT perfect.')
