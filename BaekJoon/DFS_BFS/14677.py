from collections import deque, defaultdict

n = int(input())
drug = input()
seq = ['B', 'L', 'D']

q = deque()
q.append(drug)
visit = defaultdict(int)
res = 0
while q:
    d = q.popleft()
    if len(d) == 0:
        res = n * 3
        break    
    cnt = 3 * n - len(d) # 현재 약을 먹은 횟수
    flag = False # 약을 먹었는지의 여부
    if d[0] == seq[cnt % 3]:
        if visit[d[1:]] < cnt + 1:
            visit[d[1:]] = cnt + 1
            q.append(d[1:])
            flag = True
    if d[-1] == seq[cnt % 3]:
        if visit[d[:-1]] < cnt + 1:
            visit[d[:-1]] = cnt + 1
            q.append(d[:-1])
            flag = True
    if not flag:
        res = max(res, cnt)
print(res)

# n이 작아서 bfs로 충분히 돌아가는 문제