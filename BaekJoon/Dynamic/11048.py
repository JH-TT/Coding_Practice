import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[0] * (m + 1)] # (시작지점이 (1, 1) 끝 지점이(n, m)을 맞춰주기 위함.) + 계산도 쉽게 하기 위함.
for _ in range(n):
    maze.append([0] + list(map(int, input().split())))
candy = [[0] * (m + 1) for _ in range(n + 1)]
# (i, j)기준으로 대각선(11시방향), 왼쪽, 위쪽중에 최댓값과 합한다.
for i in range(1, n + 1):
    for j in range(1, m + 1):
        candy[i][j] = maze[i][j] + max(candy[i-1][j-1], candy[i-1][j], candy[i][j - 1])

print(candy[n][m])