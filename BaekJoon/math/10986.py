from collections import deque, defaultdict
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
remainder = defaultdict(int)

acc = 0
# 누적합을 구한다.
for i in list(map(int, input().split())):
    remainder[(acc + i) % m] += 1
    acc += i

cnt = 0
for v in remainder:
    if v == 0:
        cnt += remainder[v]
    cnt += remainder[v] * (remainder[v] - 1) // 2

print(cnt)

# 누적합을 구한 뒤
# 누적합을 하면서 각 나머지 값마다 몇 개씩 있는지 개수를 센다.
# 나머지가 0이면 그대로 더하고
# 0포함 그 외 나머지값들은 nC2를 구해서 더한다.
# 왜 그러냐면 부분 누적합을 구하는 공식이 빼는거다보니 같은 나머지끼리 빼게되면 m으로 나누어떨어지게 된다.
# 부분 누적합은 2개의 left, right 인덱스를 빼는거니 n개의 같은 나머지개수중에 2개를 선택하는 조합이 이용된다.