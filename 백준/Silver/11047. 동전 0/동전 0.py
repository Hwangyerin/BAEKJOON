n,k = map(int, input().split())
L = [int(input())]
coin = 0

#동전의 가치 리스트 생성
for i in range(n-1):
    L.insert(0,int(input()))

#k을 만드는데 필요한 동전 개수의 최솟값 구하기
for i in range(n):
    if k <= 0:
        break
    if k//L[i] >= 1:
        coin += k//L[i]
        k %= L[i]
print(coin)
