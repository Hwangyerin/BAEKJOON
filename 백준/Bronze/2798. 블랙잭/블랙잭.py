import sys
from itertools import *

n, m = [int(x) for x in sys.stdin.readline().split()]
L = [int(x) for x in sys.stdin.readline().split()]
b_sum = 0

for cases in combinations(L,3):
    temp_sum = sum(cases)
    if b_sum < temp_sum <= m:
        b_sum = temp_sum
print(b_sum)