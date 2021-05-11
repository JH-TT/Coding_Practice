a = list(map(int, input()))

count_0 = 0 # 0으로 바꾸는 경우
count_1 = 0 # 1로 바꾸는 경우

if a[0] == 1: # 첫 원소가 1이면 0이 증가, 아니면 1이 증가.
    count_0 += 1
else:
    count_1 += 1

for i in range(len(a) - 1): # 리스트 원소를 전부 확인
    if a[i] != a[i + 1]: # 만약 연속으로 나오는게 끊기면.
        if a[i + 1] == 1: # 0으로 나오다가 1이 나오면
            count_0 += 1 # 0으로 바꾸는게 1증가
        else: # 그 반대의 경우면
            count_1 += 1 # 1로 바꾸는게 1증가

print(min(count_0, count_1)) # 둘 중 적은 횟수 출력.
# 0001100 입력시
# 1 출력.