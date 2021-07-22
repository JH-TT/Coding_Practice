from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(s, cnt):
    visit = [0] * (f + 1)
    q = deque()
    q.append((s, cnt))
    visit[s] = 1

    while q:
        s, cnt = q.popleft()        

        if s == g:
            return cnt
        if 1 <= s + u <= f: # u버튼을 눌렀을 때 엘베가 움직일 수 있는 범위면 움직임.
            if not visit[s + u]:
                q.append((s + u, cnt + 1))
                visit[s + u] = 1
        if 1 <= s - d <= f: # d버튼을 눌렀을 때 마찬가지로 움직일 수 있는 범위면 움직임.
            if not visit[s - d]:
                q.append((s - d, cnt + 1))
                visit[s - d] = 1

a = bfs(s, 0)
if a == None:
    print("use the stairs")
else:
    print(a)