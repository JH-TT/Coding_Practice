from collections import defaultdict
from bisect import bisect_left

# 2 4 1 5 3
# 4 5 1 3 2
# 1 5 3 2 4

# 4 0 2 1 3 -> 위의 번호가 연결된 위치
# [1, 1, 2, 2, 3]
# 이 문제는 가장 긴 증가하는 수열을 찾는 것이다.

n = int(input())
switches = list(map(int, input().split()))
bulbs = list(map(int, input().split()))
switch_bulb = defaultdict(int)

for idx, num in enumerate(bulbs):
    switch_bulb[num] = idx

res = [1] * n
sub = []
for i in range(n):    
    if not sub:
        sub.append(switch_bulb[switches[i]])
    else:
        idx = bisect_left(sub, switch_bulb[switches[i]])
        if idx == len(sub):
            sub.append(switch_bulb[switches[i]])
        else:
            sub[idx] = switch_bulb[switches[i]]
        res[i] = idx + 1

print(len(sub))
ans = []
l = len(sub)
for i in range(n-1, -1, -1):
    if res[i] == l:
        ans.append(switches[i])
        l -= 1
print(*sorted(ans))

# 가장 긴 증가하는 부분수열 문제 (단순 길이가 아닌 수열을 구해야함)