import heapq
from collections import defaultdict

def change_num(arr: list) -> int:
    total = 0
    for i in range(len(arr)):
        total += 10 ** (len(arr) - (i + 1)) * arr[i]

    return total

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
control = [list(map(int, input().split())) for _ in range(m)]
sorted_arr = sorted(arr)

if change_num(sorted_arr) == change_num(arr):
    print(0)
    exit(0)

res_cost = defaultdict(int)
visited = defaultdict(int)

res_cost[change_num(arr)] = 0 # 값은 비용을 의미

q = []
heapq.heappush(q, [0, arr])

while q:
    cost, now = heapq.heappop(q)

    if visited[change_num(now)]:
        continue

    for l, r, c in control:
        temp = now.copy()
        next_cost = cost + c
        temp[l - 1], temp[r - 1] = temp[r - 1], temp[l - 1]

        if change_num(temp) not in res_cost:
            res_cost[change_num(temp)] = next_cost
            heapq.heappush(q, [next_cost, temp])
            continue

        if next_cost < res_cost[change_num(temp)]:
            res_cost[change_num(temp)] = next_cost
            heapq.heappush(q, [next_cost, temp])

    visited[change_num(now)] = 1

result = res_cost[change_num(sorted_arr)]
print(result if result != 0 else -1)

# 배열 자체가 어떻게 보면 노드가 되는 구조.