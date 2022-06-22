import sys

n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n-1
diff = sys.maxsize
res = []

# 이분탐색 시작
while start < end:
    distance_from_zero = arr[start] + arr[end] # 일단 start값과 end값의 합을 구해놓는다.
    if abs(distance_from_zero) < diff: # 0으로부터 더 가깝다면 업데이트
        res = [arr[start], arr[end]]
        diff = abs(distance_from_zero)
    if distance_from_zero > 0: # start와 end의 절댓값중 end의 값이 더 크거나 서로 양수일 경우 -> 값을 낮춰준다.
        end -= 1
    elif distance_from_zero < 0: # start가 더 크거나, 서로 음수인 경우 -> 값을 올려준다.
        start += 1
    else: # 0이면 더이상 볼 필요 없음.
        break
print(*res)

# 절댓값에만 집중한 나머지 단순 합으로 계속 좁혀나가는 것을 생각하지 못했음....