import heapq

def solution(board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n = len(board)
    
    track = []
    q = []
    heapq.heappush(q, (0, [0, 0], [0, 1]))
    
    while q:
        cnt, r1, r2 = heapq.heappop(q)
        if [r1, r2] in track:
            continue
        if [n-1, n-1] == r1 or [n-1, n-1] == r2:
            return cnt
        r1_x, r1_y = r1
        r2_x, r2_y = r2
        # 평행이동
        for i in range(4):
            nr1_x = r1_x + dx[i]
            nr1_y = r1_y + dy[i]
            nr2_x = r2_x + dx[i]
            nr2_y = r2_y + dy[i]
            # 범위 내에 있는지 확인
            if not check(nr1_x, nr1_y, n) or not check(nr2_x, nr2_y, n):
                continue
            # 벽이 있는지 확인
            if board[nr1_x][nr1_y] == 1 or board[nr2_x][nr2_y] == 1:
                continue
            heapq.heappush(q, (cnt+1, [nr1_x, nr1_y], [nr2_x, nr2_y]))
        # 회전이동 (시계, 반시계 90도 회전을 다 구한다.)
        clock = [1, -1]
        # 가로로 놓인 경우
        if r1_x == r2_x:
            # 왼쪽이 축인 경우
            for c in range(2):
                nr2_x = r1_x + clock[c]
                nr2_y = r1_y
                if not check(nr2_x, nr2_y, n) or board[nr2_x][nr2_y] == 1:
                    continue
                if not check(r1_x+clock[c], r1_y+1, n) or board[r1_x+clock[c]][r1_y+1] == 1:
                    continue
                nxt = sorted([[r1_x, r1_y], [nr2_x, nr2_y]])
                heapq.heappush(q, (cnt+1, nxt[0], nxt[1]))
            # 오른쪽이 축인 경우
            for c in range(2):
                nr1_x = r2_x + clock[c]
                nr1_y = r2_y
                if not check(nr1_x, nr1_y, n) or board[nr1_x][nr1_y] == 1:
                    continue
                if not check(r2_x + clock[c], r2_y-1, n) or board[r2_x+clock[c]][r2_y-1] == 1:
                    continue
                nxt = sorted([[r2_x, r2_y], [nr1_x, nr1_y]])
                heapq.heappush(q, (cnt+1, nxt[0], nxt[1]))
        # 세로인 경우
        else:
            # 위가 축인 경우
            for c in range(2):
                nr2_x = r1_x
                nr2_y = r1_y + clock[c]
                if not check(nr2_x, nr2_y, n) or board[nr2_x][nr2_y] == 1:
                    continue
                if not check(r1_x+1, r1_y+clock[c], n) or board[r1_x+1][r1_y+clock[c]] == 1:
                    continue
                nxt = sorted([[r1_x, r1_y], [nr2_x, nr2_y]])
                heapq.heappush(q, (cnt+1, nxt[0], nxt[1]))
            # 아래가 축인 경우
            for c in range(2):
                nr1_x = r2_x
                nr1_y = r2_y + clock[c]
                if not check(nr1_x, nr1_y, n) or board[nr1_x][nr1_y] == 1:
                    continue
                if not check(r2_x-1, r2_y+clock[c], n) or board[r2_x-1][r2_y+clock[c]] == 1:
                    continue
                nxt = sorted([[r2_x, r2_y], [nr1_x, nr1_y]])
                heapq.heappush(q, (cnt+1, nxt[0], nxt[1]))
        track.append([r1, r2])

            
def check(x, y, n):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    return True

# 회전부분은 하나의 함수로 묶고 싶었지만 코드 자체가 어렵지 않고
# 오히려 함수로 묶을 경우 매개변수가 많아서 더욱 알아보기 힘들거 같아서 그냥 뒀다.