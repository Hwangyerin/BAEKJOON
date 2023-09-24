S = input()
D ={}
for i in range(97,123):
    D[chr(i)] = 0

for i in range(len(S)):
    if S[i] in D:
        D[S[i]] += 1
D = list(D.values())

for i in D:
    print(i, end=' ')
