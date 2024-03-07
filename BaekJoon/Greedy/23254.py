import heapq

n, m = map(int, input().split())

total_time = 24 * n

now_score = list(map(int, input().split())) # 받을 수 있는 최소 점수
add_score = list(map(int, input().split())) # 1시간마다 상승하는 점수

q = []
for idx, val in enumerate(add_score):
    heapq.heappush(q, [-val, now_score[idx]])

res = 0
while total_time > 0 and q:
    add_score, score = heapq.heappop(q)
    t = min((100 - score) // -add_score, total_time)
    new_score = score - add_score * t
    total_time -= t
    # 만약 100점이 된다면 res에 100을 더하고 q에 더이상 넣지 않는다
    if new_score == 100:
        res += 100
    # 100점이 안된다면 남은 점수를 add_score로 업데이트 시키고 다시 넣는다.
    else:
        heapq.heappush(q, [new_score-100, new_score])
# q에 남은 점수들을 더한다.
while q:
    a, b = heapq.heappop(q)
    res += b
print(res)