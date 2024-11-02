# 전시 순서는 정해지기 때문에 결론적으로 우리가 확인해야할 부분은
# 출입구를 a라고 한다면
# 모든 |p1 - a|, |pk - a| 각각 최솟값이 되는 최적의 값을 구한다.
# 즉, 모든 고양이들의 p1과 pk의 중간값을 정하면 된다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 각 겹치는 개수
cnt = [0 for _ in range(m + 1)]
ext = set()
for _ in range(n):
    kit = list(map(int, input().split()))[1:]
    ext.add(kit[0])
    ext.add(kit[-1])
    cnt[kit[0]] += 1
    cnt[kit[-1]] += 1

ext = sorted(list(ext))
res_num = ext[0]
left_right_total_dist = [0, 0] # 출입구 기준 왼쪽, 오른쪽 거리 합
left_right = [0, sum(cnt[ext[0]+1:])] # 출입구 기준 왼쪽 전시관 개수, 오른쪽 전시관 개수

# 현재 총 거리를 구한다.
for i in ext[1:]:
    left_right_total_dist[1] += (i - ext[0]) * cnt[i]
dist = sum(left_right_total_dist)

# 출입구를 하나씩 바꾸면서 거리를 계산한다.
for i in range(1, len(ext)):
    diff = ext[i] - ext[i-1] # 다음 출입구까지 거리
    left_right_total_dist[0] += (left_right[0] + cnt[ext[i-1]]) * diff # 왼쪽의 경우 거리가 늘어난다.
    left_right_total_dist[1] -= left_right[1] * diff # 오른쪽의 경우 거리가 줄어든다.

    left_right[0] += cnt[ext[i-1]]
    left_right[1] -= cnt[ext[i]]

    if sum(left_right_total_dist) < dist:
        dist = sum(left_right_total_dist)
        res_num = ext[i]

print(res_num)


# 간단한 코드
# 보통 이렇게 사이에 최솟값을 정하려면 중간값이 최솟값이 된다.
# 그래서 각 고양이별로 start, end 가 있기 때문에 N마리의 고양이는 2N개의 출입구 후보가 생긴다.
# 그래서 2N개의 출입구를 나열한뒤 정렬하고 N번째 전시회관이 거리 최솟값이되는 출입구 번호가 된다.
import sys

ip = lambda : map(int, sys.stdin.readline().split())

N, M = ip()

arr = [0] * (N*2)

for i in range(N):
    k, first, *_, end = ip()
    arr[i*2] = first
    arr[i*2+1] += end

arr.sort()
print(arr[N-1])