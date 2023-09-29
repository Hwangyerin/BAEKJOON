a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if sum(a) > sum(b):
    print(sum(a))
elif sum(a) < sum(b):
    print(sum(b))
else:
    print(sum(b))
