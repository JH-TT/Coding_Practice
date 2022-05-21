import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end, visit):
    q = deque([(start, [])])
    while q:
        now, track = q.popleft()
      
        if now == end:
            return track

        for i in road[now]:
            if visit[i] == 0:
                visit[i] = 1
                q.append((i, track + [i]))

n, m = map(int, input().split())

road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)
  
# 같은 길이여도 경로를 사전순으로 보기때문에 미리 정렬해 둔다.
for i in range(1, n + 1):
    road[i].sort()

s, e = map(int, input().split())

visit = [0] * (n + 1)
visit[s] = 1
path = bfs(s, e, visit)

visit = [0] * (n + 1)
for i in path:
    visit[int(i)] = 1
path_ = bfs(e, s, visit)

print(len(path) + len(path_))

# 문자열로 처리하다보니 두자리 이상 숫자들때문에 푸는데 오래걸림..... 그래서 리스트로 변경.