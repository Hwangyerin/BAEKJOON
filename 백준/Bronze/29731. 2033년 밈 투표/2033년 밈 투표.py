L=['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']
check = 'No'
n=int(input())

for i in range(n):
    m=input()
    if m in L:
        check='No'
    else:
        check='Yes'
        break
print(check)
