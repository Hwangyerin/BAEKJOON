from string import ascii_lowercase as alphabet
n = int(input())
L = list(alphabet)
ans = ''
CNT = [0 for x in range(26)] #알파벳 개

for i in range(n):
    name = input()
    CNT[L.index(name[0])] += 1

for i in range(26):
    if CNT[i] >= 5:
        ans += L[i]
if ans:
    print(ans)
else:
    print("PREDAJA")