import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
shot = list(map(int, input().split()))
shot.sort()
print(shot)
animal = [tuple(map(int, input().split())) for _ in range(n)]
animal.sort()
print(animal)
cnt = 0

for ani in animal:
    start = 0
    end = len(shot) - 1
    while start < end:
        mid = (start + end) // 2
        if shot[mid] < ani[0]:
            start = mid + 1
        else:
            end = mid
    # 여길 빠져나오면 사대의 위치값이 더 클것이다. 그러니 왼쪽 사대도 확인해 봐야한다.
    if abs(shot[end] - ani[0]) + ani[1] <= l or abs(shot[end - 1] - ani[0]) + ani[1] <= l:
        cnt += 1
print(cnt)
# 각 동물들이 사대의 거리안에 있는지를 이분탐색으로 확인하고 거리에 있으면 카운트하는 식으로 한다.