string =  input().upper()
D = {}
sum1 = 0
for i in range(len(string)):
    if string[i] in D:
        D[string[i]] += 1
    elif i not in D:
        D[string[i]] = 1
max_key = max(D, key = D.get)

for i in D.values():
    if i == max(D.values()):
        sum1 += 1
if sum1 > 1:
    print('?')
else:
    print(max_key)