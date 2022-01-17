from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def bfs():
    q = deque()        
    q.append(1)
    visit[1] = 1

    while q:
        n = q.popleft()
        for i in edge[n]:
            if not visit[i]:
                visit[i] = visit[n] + 1
                child[n].append(i)
                q.append(i)

n = int(input())
edge = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
child = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
seq = list(map(int, input().split()))

if seq[0] != 1:
    print(0)
else:
    bfs()

    q = deque()
    q.append(1)
    idx = 1
    while q:
        node = q.popleft()

        a = set(child[node])
        b = seq[idx:idx+len(a)]
        q.extend(b)

        if a != set(b):
            print(0)
            break
        idx += len(a)
        
    if idx == n:
        print(1)

# 풀이 방법.
# 먼저 bfs를 돌면서 각 부모노드의 자식노드를 설정한다.
# 그 뒤에 주어진 순서(일부 즉, 슬라이싱)와 자식노드들이 같은지 비교를 하고 만약 다르면 순서가 틀렸다는 의미이므로 0을 출력해서 끝낸다.