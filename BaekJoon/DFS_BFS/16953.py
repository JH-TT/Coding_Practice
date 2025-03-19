from collections import deque, defaultdict

A, B = map(int, input().split())

# 2를 곱하거나, 뒤에 1을 붙인다는것은 10을 곱하고 1을 더한다는 의미이다.
# 그래서 A가 아무리 작아도 최대 10^9라도 충분히 완탐으로 확인이 가능하다.

visit = defaultdict(lambda: False)
q = deque()
q.append((A, 0))
flag = True
while q:
    now, cnt = q.popleft()

    if now > B or (now in visit and visit[now]):
        continue

    if now == B:
        flag = False
        print(cnt + 1)
        break

    visit[now] = True
    q.append((now * 2, cnt + 1))
    q.append((now * 10 + 1, cnt + 1))

if flag:
    print(-1)

# 평범한 BFS 문제