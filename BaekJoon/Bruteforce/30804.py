from collections import Counter

n = int(input())
arr = list(map(int, input().split()))

start = 1
end = n
res = 1
while start <= end:
    mid = (start + end) // 2

    cnt_start = 0
    cnt_end = mid

    flag = False
    cnt = Counter(arr[cnt_start:cnt_end])
    while cnt_end <= n:
        if len(cnt) <= 2:
            res = max(res, cnt_end - cnt_start)
            flag = True
            break

        if cnt_end == n:
            break

        cnt[arr[cnt_start]] -= 1
        if cnt[arr[cnt_start]] == 0:
            del cnt[arr[cnt_start]]
        if not cnt.get(arr[cnt_end]):
            cnt[arr[cnt_end]] = 0
        cnt[arr[cnt_end]] += 1

        cnt_start += 1
        cnt_end += 1

    if flag:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# 완탐을 이용한 풀이
# 탕후루의 번호는 1 ~ 9까지이고, 최대 서로 다른 번호가 2개까지다.
# 즉, 최대 9C2의 경우의 수 x 최대 20만을 해도 충분히 완탐이 가능하다.
# 먼저 번호 2개를 지정하고, 그 번호 2개의 최대 연속으로 있는 개수를 구하는 방식으로 진행한다.
from itertools import combinations

n = int(input())
arr = list(map(int, input().split()))

res = 0
for case in list(combinations(set(arr), min(2, len(set(arr))))):
    cnt = 0
    for h in range(n):
        if arr[h] in case:
            cnt += 1
        else:
            res = max(cnt, res)
            cnt = 0
    res = max(cnt, res)
print(res)