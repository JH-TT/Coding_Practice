import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alphabet = []
visit = [[False] * m for _ in range(n)] # 입력받은 알파벳 중복체크
result = 0
rep = [False] * 26 # 26개의 알파벳 중복체크

for _ in range(n):
    alphabet.append(list(map(lambda a:ord(a) - 65, input())))

visit[0][0] = True
rep[alphabet[0][0]] = True
count = 1

# 백트레킹 이용.
def dfs(x, y):
    global count, result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 알파벳과 입력받은 알파벳 둘 다 중복이아니면 방문처리.
        if 0 <= nx < n and 0 <= ny < m and (not rep[alphabet[nx][ny]]) and (not visit[nx][ny]):
            rep[alphabet[nx][ny]] = True
            visit[nx][ny] = True
            count += 1
            dfs(nx, ny)
            visit[nx][ny] = False
            rep[alphabet[nx][ny]] = False
            count -= 1
dfs(0, 0)
print(result)

# BFS
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global answer
    # ans에 지나간 알파벳을 집어 넣으면서 그 길이와 result를 비교해 더 큰 값을 출력하는 방법.
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and (board[nx][ny] not in ans):
                q.add((nx, ny, ans + board[nx][ny]))
                answer = max(answer, len(ans) + 1)

n, m = map(int, input().split())              
board = [list(input()) for _ in range(n)]

answer = 1
bfs(0, 0)
print(answer)