import sys
n=0
for i in range(4):
    n += int(sys.stdin.readline().rstrip())
print(n//60)
print(n%60)
