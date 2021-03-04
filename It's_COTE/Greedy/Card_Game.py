# 숫자 카드 게임(내가 쓴 답)
n, m = map(int, input().split())
array = [[] for _ in range(n)] 
# 2차원 배열 생성
big = [] # 각 행의 최솟값들을 넣을 리스트
for i in range(n):
    array[i] = list(map(int, input().split())) # 각 행마다 정수 입력
    big.append(min(array[i])) # 그 행의 최솟값을 big리스트에 저장
print(max(big)) # 그 중에 가장 큰 수를 출력.

# 책
n, m =map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    result = max(min_value, result) # 가장 작은 수들 중에서 가장 큰 수 찾기
print(result)  # 최종 답안 출력