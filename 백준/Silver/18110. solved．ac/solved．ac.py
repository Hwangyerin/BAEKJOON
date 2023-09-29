import sys

n = int(sys.stdin.readline().rstrip()) #난이도 의견 개수

def round2(num): 
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    L = []
    for i in range(n):
        L.append(int(sys.stdin.readline().rstrip()))
    percent = int(round2(n*0.3/2))
    L.sort()
    #L = L[percent:-percent]
    res = 0
    for i in range(percent,n-percent):
        res+= L[i]
    
    res = res/(n-2*percent)
    print(round2(res))
