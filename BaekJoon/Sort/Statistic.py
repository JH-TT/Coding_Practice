import sys
input = sys.stdin.readline

n = int(input())
a = [[i, 0] for i in range(-4000, 4001)] # 입력되는 숫자가 절댓깂이 4000을 안넘는다고 했음.
sum = 0 # 평균구하기 위한 총점
count = 0 # 중앙값 구할때 쓰일 count
c = 0 # 중앙값
max = -4001
min = 4001
max_M = -4001 # 최빈값
Mode = -4001 # 가장 많이 나온 수.
for i in range(n):
    a[4000 + int(input())][1] += 1
for i in a:
    if i[1] > 0:
        if i[1] > max_M: # 가장 많이 나타난 정도부터 알기.
            max_M = i[1]
        if i[0] > max: # 최댓값구하기
            max = i[0]
        if i[0] < min: #최솟값 구하기
            min = i[0]
        sum += i[0] * i[1] # 숫자 * 나온 횟수
for i in a:
    if i[1] > 0:
        if count == n // 2: # 중앙 인덱스
            c = i[0]
            break
        elif count > n // 2:
            break
        c = i[0]
        count += 1 * i[1]
for i in a:
    if i[1] == max_M:
        if Mode != -4001:
            Mode = i[0]
            break
        else:
            Mode = i[0]

print(round(sum / n))
print(c)
print(Mode)
print(max - min)