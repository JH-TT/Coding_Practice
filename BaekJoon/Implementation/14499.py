def spinning_dice(d, move):
    if move == 1:
        return [d[move], 7-d[0], d[0], d[3], d[4]]
    elif move == 2:
        return [d[move], d[0], 7-d[0], d[3], d[4]]
    elif move == 3:
        return [d[move], d[1], d[2], 7-d[0], d[0]]
    else:
        return [d[move], d[1], d[2], d[0], 7-d[0]]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
n, m, x, y, k = map(int, input().split())
dice = [0] * 6
dir = [1, 3, 4, 5, 2] # 현재위치 + 동서북남
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
  
cmd = list(map(int, input().split()))

# 밑바닥 : 윗면 -> 1 : 6, 2 : 5, 3 : 4 반대도 그대로
# 북으로 이동 -> 원래 위치가 남으로 변함. 그의 반대가 북으로 됨. 동서 그대로
# 남으로 이동 -> 반대
# 동으로 이동 -> 원래가 서, 반대가 동, 북남은 그대로
# 서로 이동 -> 동의 반대
for i in cmd:
    nx = x + dx[i-1]
    ny = y + dy[i-1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    x, y = nx, ny
    dir = spinning_dice(dir, i)
    if board[x][y] == 0:
        board[x][y] = dice[dir[0]-1]
    else:
        dice[dir[0]-1] = board[x][y]
        board[x][y] = 0
    print(dice[6-dir[0]])

# 그냥 주사위를 굴릴때마다 현재 위치에서 동서남북이 어떻게 변하는지 구현하면 끝