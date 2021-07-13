import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


# 상 하 좌 우
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = []

def move(x, y, d):
    cnt = 0
    # 다음이 벽 or 현재자리가 구멍이 될 때까지 반복.
    while arr[x + d[0]][y + d[1]] != "#" and arr[x][y] != "O":
        x += d[0]
        y += d[1]
        cnt += 1
        
    return x, y, cnt


def bfs(x1, y1, x2, y2, count):
    q = [(x1, y1, x2, y2, count)]
    visit.append((x1, y1, x2, y2))
    while q:
        rx, ry, bx, by, count = q.pop(0)
        if count > 10:
            return -1
        for i in d:
            nrx, nry, r_count = move(rx, ry, i) # 빨간 구슬의 움직임이 제한될 때.
            nbx, nby, b_count = move(bx, by, i) # 파란 구슬의 움직임이 제한될 때.
            if arr[nbx][nby] != "O": # 파란공이 구멍을 들어가지 않았을 때.(들어갔으면 q에 아무것도 넣지 않는다.)
                if arr[nrx][nry] == "O": # 빨간공 골인하면 count출력.
                    return count
                if nrx == nbx and nry == nby: # 서로 겹치면 가장 오래움직인 공이 한 칸 이전으로 간다.(적게 움직인 공이 먼저오기 때문.)
                    if r_count > b_count:
                        nrx, nry = nrx - i[0], nry - i[1]
                    else:
                        nbx, nby = nbx - i[0], nby - i[1]
                if (nrx, nry, nbx, nby) not in visit: # 들렀던 위치가 아니면 방문처리하고, q에 넣는다.
                    visit.append((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby, count + 1)) 
            
    return -1 # 안움직인 경우.
        

for i in range(n):
    for j in range(m):
        if arr[i][j] == "R":
            x1, y1 = i, j
        elif arr[i][j] == "B":
            x2, y2 = i, j
print(bfs(x1, y1, x2, y2, 1))

# https://wlstyql.tistory.com/72?category=852442참고