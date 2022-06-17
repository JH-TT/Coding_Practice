from collections import deque

n, k = map(int, input().split())
INF = float('inf')
res = [INF] * (100001)
q = deque()
q.append([n, 0])

while q:
    pos, cnt = q.popleft()
  
    if pos < 0 or pos > 100000: continue # 범위를 벗어나면 패스
    
    if res[pos] > cnt: # 더 적은 횟수로 pos위치로 가게되면 갱신
        res[pos] = cnt
        if pos == k: continue # 동생이 있는곳이면 횟수만 갱신하고 더이상 탐색x
        q.append([pos+1, cnt+1])
        q.append([pos-1, cnt+1])
        q.append([pos*2, cnt+1])
print(res[k])