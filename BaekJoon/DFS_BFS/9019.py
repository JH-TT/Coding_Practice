from collections import deque
import sys
input = sys.stdin.readline

# DSLR 연산 해주는 함수
def change(n, type):
    if type == "D":
        return (2*n) % 10000
    elif type == "S":
        return (n-1) % 10000
    elif type == "L":
        head = n // 1000
        return (n*10 + head) % 10000
    elif type == "R":
        tail = n % 10
        return (n // 10 + tail * 1000) % 10000

move = ["D", "S", "L", "R"]
for _ in range(int(input())):
    s, e = map(int, input().split())
    visit = [0] * 10000
    q = deque()
    q.append(("", s))
    visit[s] = 1
    while q:
        track, now = q.popleft()
        if now == e:
            print(track)
            break
        for i in range(4):
            next = change(now, move[i])
            if not visit[next]:
                visit[next] = 1
                q.append((track+move[i], next))


# 기존 BFS문제와 다를게 없는데 시간초과가 까다로운 문제.