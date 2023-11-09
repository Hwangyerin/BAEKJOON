while True:
    n=int(input())
    if n == 0 :
        break
    L=[]
    for i in range(n):
        L.append(input())
    L.sort(key=str.lower)
    print(L[0])
