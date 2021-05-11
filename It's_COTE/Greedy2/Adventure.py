# 모험가 길드
# 접근 : 일단 공포도를 오름차순으로 정렬한다. 그룹의 수가 최대로 돼야하기 때문에, 일단 공포도가 가장 낮은 모험가 부터 확인하면서, 그룹에 포함될 모험가의 수를 계산한다.
n = int(input())
data = list(map(int, input().split()))

data.sort() # 현재 그룹에 포함된 모험가의 수
result = 0
count = 0
for i in data: # 공포도가 낮은 것부터 하나씩 확인
    count += 1 # 현재 그룹에 해당 모험가 포함
    if i <= count: # 조건에 맞게 되면
        result += 1 # 그룹 하나 추가
        count = 0 # 다시 모험가수 0명
print(result)