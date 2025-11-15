import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        nxt = find_parent(parent[x])
        parent[x] = nxt
    return parent[x]

def union_parent(x, y):
    px = find_parent(x)
    py = find_parent(y)

    if px < py:
        parent[py] = px
        candy[px] += candy[py]
        candy[py] = 0
        group_cnt[px] += group_cnt[py]
        group_cnt[py] = 0
    else:
        parent[px] = py
        candy[py] += candy[px]
        candy[px] = 0
        group_cnt[py] += group_cnt[px]
        group_cnt[px] = 0



n, m, k = map(int, input().split())
candy = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
group_cnt = [0] + [1 for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())

    if find_parent(x) != find_parent(y):
        union_parent(x, y)

for i in range(1, n + 1):
    find_parent(i)

groups = []
for i in range(1, n + 1):
    if group_cnt[i] > 0:
        groups.append((group_cnt[i], candy[i]))

dp = [0] * (k + 1)
for weight, value in groups:
    for w in range(k, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)

print(dp[k - 1])

# union_find + Knapsack 문제
# union_find를 이용해서 그룹지게되면 우리가아는 전형적인 냅색 형태의 문제로 바뀐다. 그 다음 냅색알고리즘 사용하면 끝.