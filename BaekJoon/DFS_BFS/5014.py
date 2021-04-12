from collections import deque

f, s, g, u, d = map(int, input().split())

def bfs(s, cnt):
    global a
    visit = [0] * (f + 1)
    q = deque()
    q.append((s, cnt))

    while q:
        s, cnt = q.popleft()
        visit[s] = 1

        if s == g:
            if cnt < a:
                a = cnt
            break
        if s + u <= g: # g보다 작거나 같으면 append
            if not visit[s + u]:
                q.append((s + u, cnt + 1))
        elif s + u > g: # g보다 커지는 경우는 내려가는걸 선택.
            if s - d >= 1:
                if not visit[s - d]:
                    q.append((s - d, cnt + 1))
        elif s - d >= g: # u와 같은방식.
            if not visit[s - d]:
                q.append((s - d, cnt + 1))
        elif s - d < g:
            if s + u <= f:
                if not visit[s + u]:
                    q.append((s + u, cnt + 1))


a = 1000000
bfs(s, 0)
if a == 1000000:
    print("use the stairs")
else:
    print(a)