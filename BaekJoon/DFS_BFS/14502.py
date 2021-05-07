# copy라이브러리를 이용해 원리 리스트를 그대로 바로 복사.
import copy

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
# 바이러스 전파시키기.
def virus(x, y, temp):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위에 있다면 주위에 0이있는지 확인후 dfs실행.
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny, temp)

# 안전지역 크기 구하기.
def get_score(temp):
    score = sum(i.count(0) for i in temp)
    return score

def dfs(start, cnt):
    global result
    # 벽 3개면 바이러스 전파시켜보고 안전지대 크기 구하기.
    if cnt == 3:
        temp = copy.deepcopy(a)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j, temp)
        result = max(result, get_score(temp))
        return
    # 연구소 벽 세우는 모든 경우 돌리기.
    for i in range(start, n * m):
        x = i // m
        y = i % m
        if a[x][y] == 0:
            a[x][y] = 1
            dfs(i, cnt + 1)
            a[x][y] = 0
dfs(0, 0)
print(result)

# 시작점부터 끝까지 가능한 모든 좌표 방문. <- 아 부분이 좀 까다로웠음.
# 방법1) 그냥 for문으로 하기
# for i in range(n):
#   for j in range(m):
#       if a[i][j] == 0:
#           a[i][j] = 1
#           dfs(cnt)
#           a[i][j] = 0
#           cnt -= 1 이런식.
# 방법 2) 몫과 나머지 구하는 형식으로 하기
# for i in range(start, n * m):
#     x = i // m # 몫을 구하는 것. 즉 리스트에선 행을 나타냄.
#     y = i % m  # 나머지 구하기. 리스트에선 열을 나타냄.