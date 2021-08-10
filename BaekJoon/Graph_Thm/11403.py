from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
node = [list(map(int, input().split())) for _ in range(n)]

for k in range(n): # 노드를 하나씩 살펴본다.
    q = deque() # 연결된 노드들을 담을 데크.
    for i in range(n):
        if node[k][i] == 1: # 노드i랑 연결돼 있다면 q에 넣는다.
            q.append(i)
    while q: # q가 빌때까지.
        next = q.popleft() # 노드 하나를 꺼낸다.
        for j in range(n):
            if node[next][j] == 1 and not node[k][j]:  # 그 노드와 연결된 다른 노드를 본다. 단 이미 k노드와 연결된 노드제외.
                node[k][j] = 1
                if k != j: # 다시 k노드로 돌아오면 q에 넣지 않는다.
                    q.append(j)

for i in node:
    print(*i)

# 플로이드 워셜 알고리즘. 그냥 모든 경로를 살펴본다고 보면 됨. 시간복잡도는 O(N^3).