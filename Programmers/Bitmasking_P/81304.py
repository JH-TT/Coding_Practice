from collections import defaultdict
import heapq

def solution(n, start, end, roads, traps):

    def getStatus(st):
        total = 0
        for idx, tp in enumerate(traps):
            total += (2 ** idx) * int(st[d[tp]])
        return total

    INF = 10 ** 8
    graph = defaultdict(list)

    for p, q, s in roads:
        graph[p].append((s, q, 0))
        if (p in traps) or (q in traps):
            graph[q].append((s, p, 1))

    # 방문처리
    visit = [[INF for _ in range(n + 1)] for _ in range(2 ** len(traps))]

    d = defaultdict(int) # 해당 트랩이 몇번째 비트인지
    for idx, t in enumerate(traps):
        d[t] = idx

    status = "0" * len(traps)
    h = []
    heapq.heappush(h, (0, start, status))
    visit[start][0] = 0
    res = INF

    while h:
        c, now, trap_status = heapq.heappop(h)

        # 탈출하면 res 업데이트
        if now == end:
            res = min(res, c)
            continue

        if now in traps:
            now_bit = int(trap_status[d[now]]) # 현재 트랩 상태를 저장
        else:
            now_bit = 0

        for nxt_c, nxt, onOff in graph[now]:
            # 다음 정점의 트랩 상태를 가져온다.
            if nxt in traps:
                nxt_bit = int(trap_status[d[nxt]])
            else:
                nxt_bit = 0

            # 트랩이 발동한 상황인데 지금 방향이 정방향인 경우
            if (now_bit ^ nxt_bit) == 1:
                if onOff == 0: continue
            else: # 트랩이 발동하지 않은 상황인데 지금 역방향인 경우
                if onOff == 1: continue

            if nxt not in traps:
                nxt_status = trap_status
            else:
                nxt_status = trap_status[:d[nxt]] + str(int(trap_status[d[nxt]]) ^ 1) + trap_status[d[nxt]+1:]

            if c + nxt_c < res:
                if visit[getStatus(nxt_status)][nxt] <= c + nxt_c:
                    continue
                visit[getStatus(nxt_status)][nxt] = c + nxt_c
                heapq.heappush(h, (c + nxt_c, nxt, nxt_status))

    return res


# 이번 문제는 비트마스킹 + BFS였다. 많이 어려웠던 문제
# 현재 정방향인지 역방향인지 체크를 하고 end까지 최소비용으로 이동하도록 하는것이 관건
# 그래서 사용하는 자료구조가 꽤 있었다.