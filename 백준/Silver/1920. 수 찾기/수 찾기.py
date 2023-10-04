import sys
N = int(sys.stdin.readline().rstrip())
A = set(map(int, sys.stdin.readline().split()))
m = int(input())
m_list = [int(x) for x in sys.stdin.readline().rstrip().split()]

for i in m_list:
    if i in A:
        print(1)
    else:
        print(0)
