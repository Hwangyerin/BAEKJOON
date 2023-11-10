n,m=[int(x) for x in input().split()]
hear = []
see = []
hearsee=[]

for i in range(n):
    hear.append(input())
for i in range(m):
    see.append(input())
hearsee = list(set(hear)&set(see))
hearsee.sort()
print(len(hearsee))
for i in hearsee:
    print(i)
