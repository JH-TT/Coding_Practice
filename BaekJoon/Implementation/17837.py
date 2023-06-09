# N x N 체스판
# 말의 개수 K개, 원판모양
# 말 위에 다른 말 올릴 수 있음
# 체스판 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠됨

# 체스판 위에 말 K개를 놓고 시작
# 1 ~ K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다. 상하좌우 4가지
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동, 위에 올려진 말도 함께 이동.
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르다.
# 말이 4개 이상 쌓이면 게임 종료

# 말이 이동하려는 칸이
#   흰색인 경우엔 그 칸으로 이동. 이동하려는 칸에 말이 이미 있는 경우 가장 위에 올린다.
#     A번 말의 위에 다른 말이 있는 경우 A번 말과 위에 있는 모든 말이 이동.
#     A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있으면 A가 이동한 이후는 D, E, A, B, C가 된다.
#   빨간색인 경우 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다. 
#     A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우 C, B, A가 된다.
#     A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다. 
#   파란색인 경우에는 A번 말의 이동 방향을 반대로하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
#   체스판을 벗어나는 경우에는 파란색과 같은 경우다. 

# 0 : 흰색, 1 : 빨간색, 2 : 파란색

import sys
input = sys.stdin.readline

# 벽인지 확인인
def check_pos(x, y):
    if x < 1 or x > N or y < 1 or y > N:
        return True
    return False

def change_pos(r, c, dir, idx):
    nr = r + dx[dir]
    nc = c + dy[dir]
    sub_arr = status[r][c][idx:]
    status[r][c] = status[r][c][:idx]
    # 벽, 파란색 이면 방향을 바꾸고 다시 확인한다. 
    if check_pos(nr, nc):
        if dir in [1, 2]:
            dir = [1, 2][([1, 2].index(dir) + 1) % 2]
        else:
            dir = [3, 4][([3, 4].index(dir) + 1) % 2]
        nr = r + dx[dir]
        nc = c + dy[dir]
        h = sub_arr[0][0]
        sub_arr[0] = (h, dir) # 방향 변경
    elif arr[nr][nc] == 2: # 파란색인 경우
        if dir in [1, 2]:
            dir = [1, 2][([1, 2].index(dir) + 1) % 2]
        else:
            dir = [3, 4][([3, 4].index(dir) + 1) % 2]
        nr = r + dx[dir]
        nc = c + dy[dir]
        h = sub_arr[0][0]
        sub_arr[0] = (h, dir) # 방향 변경
    # 여기는 if로 해야 벽 or 파란색을 만나서 방향을 변경해도 다음이 빨강인지 확인하게 된다. 
    if not check_pos(nr, nc) and arr[nr][nc] == 1: # 빨간색인 경우 순서 반대
        sub_arr = list(reversed(sub_arr))
      
    return [nr, nc, sub_arr]

# 우, 좌, 상, 하
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

N, K = map(int, input().split())
arr = [[-1] * (N+1)] + [[-1] + list(map(int, input().split())) for _ in range(N)]
status = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
chess = [()] # 각 말의 좌표

for i in range(1, K+1):
    r, c, di = map(int, input().split())
    status[r][c].append((i, di)) # (i번말, 방향)
    chess.append((r, c))

time = 1
while time <= 1000:
    # 하나씩 이동하기
    for i in range(1, K+1):
        idx, dir = 0, 0
        r, c = chess[i][0], chess[i][1]
        # 해당 말이 몇 번째 높이에 있는지 찾기
        while idx < len(status[r][c]):
            num, dir = status[r][c][idx]
            if num == i:
                break
            idx += 1
          
        nr, nc, sub_arr = change_pos(r, c, dir, idx) # 다음위치, 움직일 말의 정보들
      
        # 벽 or 파란색때문에 방향을 바꾸고도 다음칸이 파랑색 or 벽이면 다시 말을 그자리에 두고 다음으로 이동
        if check_pos(nr, nc):
            status[r][c] += sub_arr # 이동없이 그대로
            if len(status[r][c]) >= 4:
                print(time)
                exit()
            continue
        if arr[nr][nc] == 2:
            status[r][c] += sub_arr # 이동없이 그대로
            if len(status[r][c]) >= 4:
                print(time)
                exit()
            continue
        ##

        for a in sub_arr: # target말과 그 위에 있는 말 전부 좌표 변경
            chess[a[0]] = (nr, nc)
        status[nr][nc] += sub_arr # 해당 좌표로 말 전부 이동
        if len(status[nr][nc]) >= 4:
            print(time)
            exit()
    time += 1
        
print(-1)

# 구현이 꽤나 빡셌던 문제