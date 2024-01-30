d, n, m = map(int, input().split())

stone = sorted([int(input()) for _ in range(n)]) + [d]

# 이분탐색 시작
start = 0
end = d
res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0 # 돌다리 밟은 횟수
    srt = mid # 시작거리
    for i in stone:
        if srt <= i:
            srt = i + mid
            cnt += 1

    if cnt == n - m + 1:
        res = max(res, mid)
    # 만약 적게 밟았다면 -> 넓게 밟음 -> 줄인다
    if cnt < n - m + 1:
        end = mid - 1
    else:
        start = mid + 1
print(end)

# 이 문제는 비슷한 유형을 몇 번 풀어봤기에 바로 알아챔

# 1. 최소중에 최대를 찾는다.
# 2. 그런데 뭔가 정확한 값을 딱 정하기가 애매하다.
# 3. 주어지는 값이 크다.

# 보통 위에 있는 것들이 충족하면 이분탐색일 확률이 굉장히 크다.