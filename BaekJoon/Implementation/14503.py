import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
cor = [list(map(int, input().split())) for _ in range(n)]
spin = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0: 북, 1: 동, 2: 남, 3: 서
clr = 0 # 청소한 구역 개수.
while 1:
    flag = False # 4방향을 돌면서 청소구역을 찾았는지 판단하는 변수.
    if cor[r][c] == 0: # 해당자리가 청소되지 않은 경우만 청소하고 청소구역 + 1해준다.
        clr += 1
        cor[r][c] = 2
    for i in range(1, 5): # 4방향을 왼쪽으로 돌면서 청소할 공간이 있는지 확인한다.
        e = (d + 3 * i) % 4 # i가 증가할때 마다 왼쪽으로 돈다.
        x, y = spin[e] # 왼쪽 방향

        # 왼쪽 방향의 좌표들
        a = r + x
        b = c + y
        if cor[a][b] == 0: # 왼쪽 방향에 청소할 장소가 있다면 왼쪽방향의 좌표로 업데이트하고 바라보는 방향도 왼쪽 방향으로 한다.
            r, c, d = a, b, e
            flag = True # 청소구역 찾음을 뜻함.
            break
    if flag: # 왼쪽방향에 청소구역을 찾았으면 밑에코드는 스킵한다.
        continue
    # 여기를 빠져나왔다는건 4방향이 벽이거나 청소한거다.
    rear = (d + 2) % 4 # 후진
    r_x, r_y = spin[rear] # 후진방향

    # 후진할 좌표
    r_a = r + r_x
    r_b = c + r_y

    if cor[r_a][r_b] != 1: # 만약 후진할 곳이 벽이아니면 그 좌표로 이동한다. 단 바라보는 방향은 그대로(문제에 있음).
        r, c = r_a, r_b
    else: # 벽이면 그대로 종료.
        break
print(clr)
