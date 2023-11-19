import sys
k = int(sys.stdin.readline())
for i in range(1,k+1):
    gap = 0
    print('Class', i)
    L=[int(x) for x in sys.stdin.readline().rstrip().split()]
    cnt = L[0]
    L = L[1:]
    L.sort(reverse=True)
    for i in range(len(L)-1):
        tmp = L[i]-L[i+1]
        if gap < tmp:
            gap = tmp

    print('Max',max(L),end='')
    print(', Min', min(L),end='')
    print(', Largest gap',gap)