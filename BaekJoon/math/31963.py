# 처음 풀이
# 각 위치마다 2를 몇 번 곱했는지 기록해 놓고 원본값으로 개수를 더하고 빼는 방식으로 구현
# 그런데 실제 2를 제곱한 값으로 비교하는 부분이 있어서 pypy로만 통과했다.
from bisect import bisect_left
import math

n = int(input())
seq = list(map(int, input().split()))
multiCnt = [0]

res = 0
for i in range(1, n):
    cnt = 0
    if seq[i] < seq[i-1] * (2 ** multiCnt[i-1]):
        if seq[i] == seq[i-1]:
            cnt = multiCnt[i-1]
        elif seq[i] < seq[i-1]: # 왼쪽이 더 큰 경우
            div = seq[i-1] / seq[i]
            sqCnt = math.ceil(math.log2(div))
            cnt = multiCnt[i-1] + sqCnt
        else:
            div = seq[i] / seq[i-1]
            sqCnt = math.ceil(math.log2(div))
            if div == 2 ** sqCnt:
                cnt = multiCnt[i-1] - sqCnt
            else:
                cnt = multiCnt[i-1] - sqCnt + 1
    multiCnt.append(cnt)
    res += cnt
print(res)

# 다른 풀이
# 이는 처음 풀이를 효율적으로 풀이한 방식이다.
# 전체적인 틀은 처음풀이와 같은데 실제로 2제곱을 곱한 값을 비교하는 방식을 하지 않고
# 원본값만 미리 비교한 뒤에 다음 cnt에 값을 더해주는 방식으로 했다. (왜냐하면 이전값에 2를 곱했다면 바로 다음 수도 영향이 있긴 하니까...)
from bisect import bisect_left

n = int(input())
seq = list(map(int, input().split()))
cnt = [0] * (n + 1)
twoSq = [1]

for i in range(1, 21):
    twoSq.append(2 ** i)

for i in range(1, n):
    # 왼쪽이 더 큰 경우
    if seq[i] < seq[i-1]:
        multiCnt = bisect_left(twoSq, seq[i-1] / seq[i])
        cnt[i] = multiCnt
    elif seq[i] > seq[i-1]:
        multiCnt = bisect_left(twoSq, seq[i] / seq[i-1])
        if seq[i-1] * (2 ** multiCnt) > seq[i]:
            multiCnt -= 1
        cnt[i] = -multiCnt

res = 0
for i in range(1, n):
    if cnt[i] > 0:
        res += cnt[i]
        cnt[i+1] += cnt[i]
print(res)