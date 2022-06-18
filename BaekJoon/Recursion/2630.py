import sys
input = sys.stdin.readline

def dfs(n, a, b):
    global white, blue
    
    if n == 1:
        if arr[a][b]:
            blue += 1
        else:
            white += 1
        return
    color = arr[a][b]
    for i in range(n):
        for j in range(n):
            if arr[a+i][b+j] != color: # 만약 색이 한 개로 통일되지 않았다면 4등분한다.
                dfs(n//2, a, b)
                dfs(n//2, a+n//2, b)
                dfs(n//2, a, b+n//2)
                dfs(n//2, a+n//2, b+n//2)
                return
    # 한 개로 통일된 상태면 색에 따라 개수를 증가시킨다.
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

dfs(N, 0, 0)

print(white)
print(blue)