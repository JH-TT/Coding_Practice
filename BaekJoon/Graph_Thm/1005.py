import sys
import copy
from collections import deque
input = sys.stdin.readline

T = int(input())

def topology(goal):
    q = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            D[i] = max(D[i], D_2[i] + D[now])
            ind[i] -= 1
            if ind[i] == 0:
                q.append(i)

for _ in range(T):
    res = 0
    n, k = map(int, input().split())
    D = [0] + list(map(int, input().split()))
    D_2 = copy.deepcopy(D)
    ind = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1
    W = int(input())
    topology(W)
    print(D[W])

# 간단한 위상정렬 + DP 문제.
# DP는 어느 건물을 짓기위한 시간을 결정할때 사용.