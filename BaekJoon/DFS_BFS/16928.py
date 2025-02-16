from collections import deque, defaultdict
import sys
input = sys.stdin.readline

ladder = defaultdict(int)
snake = defaultdict(int)
INF = 10 ** 6

n, m = map(int, input().split())

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

visit = [INF for _ in range(101)]
q = deque()
q.append(1)
visit[1] = 0

while q:
    now = q.popleft()

    if now == 100:
        print(visit[100])
        break

    # 주사위 굴리기 (1 ~ 6)
    for i in range(1, 7):
        nxt = now + i

        if nxt > 100:
            break

        # 이미 더 적은 횟수로 지났던 길이면 진행x
        if visit[nxt] <= visit[now] + 1:
            continue

        visit[nxt] = visit[now] + 1

        #사다리, 뱀을 확인한다.
        if nxt in ladder:
            nxt_ladder = ladder[nxt]
            if visit[nxt] < visit[nxt_ladder]:
                visit[nxt_ladder] = visit[nxt]
                q.append(nxt_ladder) # 최종적으로 사다리로 이동한 위치가 다음위치가 된다.
            continue

        if nxt in snake:
            nxt_snake = snake[nxt]
            if visit[nxt] < visit[nxt_snake]:
                visit[nxt_snake] = visit[nxt]
                q.append(nxt_snake) # 최종적으로 뱀으로 이동한 위치가 다음위치가 된다.
            continue

        q.append(nxt)

# BFS 문제.
# 사다리 혹은 뱀에 도착했을때, 사다리 또는 뱀으로 이동한 위치가 q에 들어가야 한다.
# 그런데 만약 사다리 또는 뱀으로 이동한 위치가 더 적은 주사위 횟수로 이미 이동했다면 q에 넣으면 안된다.
# 즉, 뱀 또는 사다리를 만났다면 바로 continue를 해야한다. (50, 57라인)