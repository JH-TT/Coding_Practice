from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
if k < n:
    print(n - k)
    print(1)
elif n == k:
    print(0)
    print(1)
else:
    INF = 10 ** 6
    cnt = defaultdict(int) # key: 이동횟수, cnt: 경우의 수
    visit = [INF] * 200001
    visit[n] = 0

    q = deque()
    q.append((n, 0)) # 현재 위치, 이동 횟수

    while q:
        now, move = q.popleft()
        if now == k:
            cnt[move] += 1
            continue

        plus_one = now + 1
        minus_one = now - 1
        double_move = now * 2

        if plus_one <= 200000 and move + 1 <= visit[plus_one]:
            visit[plus_one] = move + 1
            q.append((plus_one, move + 1))

        if minus_one >= 0 and move + 1 <= visit[minus_one]:
            visit[minus_one] = move + 1
            q.append((minus_one, move + 1))

        if double_move <= 200000 and move + 1 <= visit[double_move]:
            visit[double_move] = move + 1
            q.append((double_move, move + 1))

    for first in cnt:
        print(first)
        print(cnt[first])
        break
# BFS 풀이

# BFS 다른 풀이 최적화 적용
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([n])
visit = [-1] * 200001
cnt = [0] * 200001

visit[n] = 0
cnt[n] = 1

while q:
    now = q.popleft()

    if now == k:
        print(visit[k])
        print(cnt[k])
        exit(0)

    for nxt in (now - 1, now + 1, now * 2):
        if 0 <= nxt <= 200000:
            if visit[nxt] == -1:
                visit[nxt] = visit[now] + 1
                cnt[nxt] = cnt[now]
                q.append(nxt)
            elif visit[nxt] == visit[now] + 1:
                cnt[nxt] += cnt[now]
print(visit[k])
print(cnt[k])
# 내 풀이와 다른점은
# 내 풀이의 경우 같은 횟수에 대해 1씩 증가하지만
# 이 풀이는 k로 오기 이전 위치로 가는 경우의 수를 뭉친다음 한 번에 더해주는 방식이었다.
# 그래서 아래 풀이가 훨씬 빨랐다.