from collections import deque

# 에라토스테네스의 체를 이용해서 미리 소수들을 구해놓는다.
INF = 10000
eratos = [True for _ in range(INF)]
eratos[0] = False
eratos[1] = False

for i in range(2, int(INF ** 0.5) + 1):
    if eratos[i] == False: continue
    j = 2
    while i * j < INF:
        eratos[i * j] = False
        j += 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    visit = [0 for _ in range(INF)]
    q = deque()    
    q.append((a, 0))
    visit[a] = 1
    flag = False

    while q:
        now, cnt = q.popleft()
        if now == b:
            print(cnt)
            flag = True
            break
        # 천, 백, 십, 일 하나씩 바꾸기
        th = now // 1000
        hun = (now % 1000) // 100
        ten = (now % 100) // 10
        one = now % 10

        # 천
        for i in range(1, 10):
            nxt = i * 1000 + hun * 100 + ten * 10 + one
            if visit[nxt] == 0 and eratos[nxt]:
                q.append((nxt, cnt + 1))
                visit[nxt] = 1
        # 백
        for i in range(10):
            nxt = th * 1000 + i * 100 + ten * 10 + one
            if visit[nxt] == 0 and eratos[nxt]:
                q.append((nxt, cnt + 1))
                visit[nxt] = 1
        # 십
        for i in range(10):
            nxt = th * 1000 + hun * 100 + i * 10 + one
            if visit[nxt] == 0 and eratos[nxt]:
                q.append((nxt, cnt + 1))
                visit[nxt] = 1
        # 일
        for i in range(10):
            nxt = th * 1000 + hun * 100 + ten * 10 + i
            if visit[nxt] == 0 and eratos[nxt]:
                q.append((nxt, cnt + 1))
                visit[nxt] = 1
    if not flag:
        print("Impossible")

# 이 문제는 주어진 제한덕분에 순수 bfs로 풀렸다.
# 1. 소수여야 함
# 2. 4자리 숫자임(가장 앞자리가 0이 아님)
# 3. 한 자리씩만 숫자를 바꿀 수 있음

# 위 세 가지 조건을 토대로 생각해 보면
# 각 자릿수를 하나씩 바꿔가면서 확인해도 40 * 10000 보다 적게 나올 것이기 때문에 가능하다.