import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
wires = [list(map(int, input().split())) for _ in range(n)]
wires.sort(key=lambda x: x[1])

a_wires = [a for a, _ in wires]

lis = []
lis_idx = [0] * n

for i, a in enumerate(a_wires):
    pos = bisect_left(lis, a)
    if pos == len(lis):
        lis.append(a)
    else:
        lis[pos] = a
    lis_idx[i] = pos

target = len(lis) - 1
lis_set = set()

for i in range(n - 1, -1, -1):
    if lis_idx[i] == target:
        target -= 1
    else:
        lis_set.add(wires[i][0])

print(len(lis_set))
for a in sorted(list(lis_set)):
    print(a)

# LIS + 역추적 문제
# 그냥 길이를 구하는 문제였으면 쉽게 풀었겠지만 이번껀 어떤 값을 제외할건지 찾아야하는 역추적이 필요했다.