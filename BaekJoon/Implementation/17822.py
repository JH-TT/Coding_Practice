import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    visit[x][y] = 1
    c = 1
    for i in range(4):
        nx = x + dx[i]
        ny = (y + dy[i]) % M
        if nx < 1 or nx > N:
            continue
        if visit[nx][ny] or arr[nx][ny] != arr[x][y]:
            continue
        c += dfs(nx, ny)
    arr[x][y] = "x"
    return c

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

total = 0
num_cnt = 0
N, M, T = map(int, input().split())
arr = [[-1] * M] # 디스크 번호를 맞추기 위함

for _ in range(N):
    disk = list(map(int, input().split()))
    total += sum(disk)
    num_cnt += M
    arr.append(disk)

# 번호가 x의 배수인 원판을 d방향으로 k칸 회전
# d가 0인 경우 : 시계 방향
# d가 1인 경우 : 반시계 방향
for _ in range(T):
    x, d, k = map(int, input().split())
    if num_cnt == 0:
        break
    idx = 1
    while x * idx <= N:
        if d == 0:
            sub_arr = arr[x*idx][M-k:]
            arr[x*idx] = arr[x*idx][:M-k]
            arr[x*idx] = sub_arr + arr[x*idx]
        else:
            sub_arr = arr[x*idx][:k]
            arr[x*idx] = arr[x*idx][k:]
            arr[x*idx] += sub_arr
        idx += 1
    # 인접한 숫자 빼기
    visit = [[0] * M for _ in range(N+1)]
    mean = 0
    total_cnt = 0
    for i in range(1, N+1):
        for j in range(M):
            cnt = 0
            v = arr[i][j]
            if arr[i][j] == "x":
                continue
            if not visit[i][j]:
                cnt = dfs(i, j)
            if cnt == 1:
                arr[i][j] = v
            else:
                total -= v * cnt
                num_cnt -= cnt
                total_cnt += 1
    if total_cnt != 0:
        continue
    mean = total / num_cnt
    for i in range(1, N+1):
        for j in range(M):
            if arr[i][j] == "x":
                continue
            if arr[i][j] < mean:
                arr[i][j] += 1
                total += 1
            elif arr[i][j] > mean:
                arr[i][j] -= 1
                total -= 1
print(total)