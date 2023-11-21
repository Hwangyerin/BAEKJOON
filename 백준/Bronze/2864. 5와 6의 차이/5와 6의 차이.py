import sys

n,m = sys.stdin.readline().rstrip().split()

min_n=int(n.replace('6','5'))+int(m.replace('6','5'))
max_n=int(n.replace('5','6'))+int(m.replace('5','6'))
print(min_n,max_n)
