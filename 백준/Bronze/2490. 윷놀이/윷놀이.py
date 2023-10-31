for i in range(3):
    L=[int(x) for x in input().split()]
    if L.count(0)==1:
        print('A')
    elif L.count(0)==2:
        print('B')
    elif L.count(0)==3:
        print('C')
    elif L.count(0)==4:
        print('D')
    elif L.count(1)==4:
        print('E')

    
