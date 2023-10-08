import sys
level = ['A+','A0','B+','B0','C+','C0','D+','D0','F']
grade = [4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0.0]

total = 0
result = 0
for i in range(20):
    s,c,t = map(str, sys.stdin.readline().split())
    c = float(c)
    if t != 'P':
        total+=c
        result += c*grade[level.index(t)]
print(round(result/total,6))
