n = int(input())
result = 0
sum1 = 0
for i in range(n):
    word = input()
    L=[word[0]]
    for j in range(len(word)):
        if word[j] not in L:
            L.append(word[j])
            result = 1
        elif word[j] in L and L[-1] != word[j]:
            result = 0
            break
        elif word[j] in L and L[-1] == word[j]:
            L.append(word[j])
            result = 1
    if result == 1:
        sum1 += 1
print(sum1)
