import sys
n = int(input())
bookD = {}
answer = []
for i in range(n):
    book = sys.stdin.readline().rstrip()
    if book in bookD:
        bookD[book] += 1
    else:
        bookD[book] = 1
maxValue = max(bookD.values())
for k in bookD.keys():
    if bookD[k] == maxValue:
        answer.append(k)
answer.sort()
print(answer[0])
