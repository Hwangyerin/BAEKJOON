import sys
temp = 0
result = 0
cnt=0
for i in range(10):
    L=(int(sys.stdin.readline()))
    temp=result
    result+=L
    if result >= 100:
        break
if abs(100-temp)>=abs(100-result):
    print(result)
else:
    print(temp)
