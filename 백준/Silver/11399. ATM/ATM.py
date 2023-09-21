n = int(input()) #사람 수
time = [int(x) for x in input().split()] #각 사람이 돈을 인출하는데 걸리는 시간 리스트
result = 0 #각 사람이 돈을 인출하는데 필요한 시간의 합이 저장되는 변수
time.sort() #리스트 오름차순으로 정렬

for i in range(n):
    result += sum(time[0:i+1])
print(result)
