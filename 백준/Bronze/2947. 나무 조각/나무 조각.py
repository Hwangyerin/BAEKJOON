L = [int(x) for x in input().split()]
sortL = [1,2,3,4,5]

while L != sortL:
    for i in range(4):
        if L[i] > L[i+1]:
            L[i], L[i+1] = L[i+1], L[i]
            for j in range(5):
                print(L[j], end=' ')
            print()
        else:
            continue
    
