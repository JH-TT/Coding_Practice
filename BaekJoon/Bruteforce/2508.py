import sys
input = sys.stdin.readline

# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 행 열 순으로 주어짐
def find_candy(r, c):
    cnt = 0
    for i in range(r):
        for j in range(c):
            if candy[i][j] == "o":
                # 좌우
                if 0 < j < c-1:
                    if candy[i][j-1] == ">" and candy[i][j+1] == "<":
                        cnt += 1
                        continue
                # 상하
                if 0 < i < r-1:
                    if candy[i-1][j] == "v" and candy[i+1][j] == "^":
                        cnt += 1
                        continue
    return cnt
                    

for _ in range(int(input())):
    _ = input().rstrip()
    r, c = map(int, input().split())
    candy = [list(input().rstrip()) for _ in range(r)]
    print(find_candy(r, c))

# 완탐문제