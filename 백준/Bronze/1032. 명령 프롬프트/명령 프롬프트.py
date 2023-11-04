n = int(input())
word1=list(input())
for i in range(n-1):
    word2=list(input())
    for j in range(len(word1)):
        if word1[j] != word2[j]:
            word1[j] = '?'
for i in word1:
    print(i,end='')
