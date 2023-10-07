n = int(input())

for i in range(n):
    case_n = 0
    avg = 0
    cnt = 0
    L = [int(x) for x in input().split()]
    case_n = L[0]
    L = L[1:]
    avg = sum(L)/case_n
    for j in L:
        if j > avg :
            cnt += 1
    print(round(float(cnt/case_n*100),3),'%',sep='')
    
        
