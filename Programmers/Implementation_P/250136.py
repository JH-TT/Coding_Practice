from collections import defaultdict, deque

def solution(land):
    answer = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    r = len(land)
    c = len(land[0])
    # 각 좌표별 구역 구분 번호
    sep_num = [[-1 for _ in range(c)] for _ in range(r)]
    # 각 구역별 석유량
    oil = defaultdict(int)

    seq = 1 # 구역 번
    for i in range(r):
        for j in range(c):
            if sep_num[i][j] != -1 or land[i][j] == 0: continue
            # 석유면 탐색 시작
            q = deque()
            q.append((i, j))
            sep_num[i][j] = seq
            cnt = 1
            while q:
                x, y = q.popleft()

                for h in range(4):
                    nx = x + dx[h]
                    ny = y + dy[h]
                    if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
                    if land[nx][ny] == 0: continue
                    if sep_num[nx][ny] != -1: continue
                    sep_num[nx][ny] = seq
                    cnt += 1
                    q.append((nx, ny))
            oil[seq] = cnt
            seq += 1

    for i in range(c):
        visit = [0] * seq
        all_cnt = 0
        for j in range(r):
            if sep_num[j][i] == -1: continue
            if visit[sep_num[j][i]] != 0: continue
            all_cnt += oil[sep_num[j][i]]
            visit[sep_num[j][i]] = 1
        answer = max(answer, all_cnt)

    return answer

# bfs로 한번에 정보들을 모아놓는것이 핵심인 문제. DAT 활용을 잘 해야 한다.