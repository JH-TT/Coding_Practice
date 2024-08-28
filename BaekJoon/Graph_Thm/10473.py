import sys, heapq
input = sys.stdin.readline

INF = float('inf')

start = list(map(float, input().split())) # 시작 좌표
end = list(map(float, input().split())) # 끝 좌표
n = int(input())
pos = [list(map(float, input().split())) for _ in range(n)] # 4개의 포탑좌표
pos = [start] + pos + [end]
_time = [INF for _ in range(n + 2)] # 시작, 끝까지 포함 0은 시작, n+1은 끝
_time[0] = 0

q = []
heapq.heappush(q, (0, 0))
while q:
    cur_t, node = heapq.heappop(q)
    if _time[node] < cur_t:
        continue
    for nxt in range(n+2):
        # 당연히 같은곳은 안됨
        if node == nxt: continue
        # 현재에서 nxt까지 거리
        cal_di = ((pos[node][0] - pos[nxt][0]) ** 2 + (pos[node][1] - pos[nxt][1]) ** 2) ** 0.5
        # 시간 구하기(1 ~ n이면 포탑임)
        if node in list(range(1, n+1)):
            c = cur_t + (2 + (abs(cal_di-50) / 5)) # 포탑은 50미터를 2초만에 날아간다
        else:
            c = cur_t + (cal_di / 5)
        if c < _time[nxt]:
            _time[nxt] = c
            heapq.heappush(q, (c, nxt))
print(_time[-1])

# 다익스트라 문제
# 다만 거리가 아닌, 시간 계산이라서 잘 보고 해야함