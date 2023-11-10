n,m=[int(x) for x in input().split()]
row = [0 for x in range(m)]
cnt = 0
for i in range(n):
    castle = input()
    if not 'X' in castle:
        cnt+=1
    for j in range(m):
        if castle[j] == 'X':
            row[j] = 1
    
print(max(cnt,row.count(0)))
