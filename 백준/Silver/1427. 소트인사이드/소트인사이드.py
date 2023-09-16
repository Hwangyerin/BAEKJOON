num = input()
L = []
for i in range(len(num)):
    L.append(int(num)%10)
    num = int(num)//10
L.sort(reverse=True)

for i in range(len(L)):
    print(L[i],end='')
    
