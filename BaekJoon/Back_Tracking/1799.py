# 백트래킹
# x와 y끼리 빼고 절댓값이 서로 같으면 같은 대각선상에 있다는 의미!
# 1은 비숍이 있을 수 있는자리, 0은 안되는 자리
import sys
input = sys.stdin.readline

def dfs(pos, bishops, level, right, left) -> int:
    cnt = len(bishops)
    for lvl in range(level + 1, len(pos)):
        p = pos[lvl]

        r = p[0] + p[1]
        l = p[0] - p[1]

        if r in right or l in left:
            continue

        # 비숍을 놓을 수 있다면 다음단계...
        bishops.append(p)
        right.add(r)
        left.add(l)
        cnt = max(cnt, dfs(pos, bishops, lvl, right, left))
        bishops.pop()
        right.remove(r)
        left.remove(l)

    return cnt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

black_pos = []
white_pos = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 0:
            continue
        # 흑
        if (i + j) % 2 == 0:
            black_pos.append((i, j))
        else:
            white_pos.append((i, j))

white_res = 0
black_res = 0
for i in range(len(black_pos)):
    used_right_diag = set()
    used_left_diag = set()

    used_right_diag.add(black_pos[i][0] + black_pos[i][1])
    used_left_diag.add(black_pos[i][0] - black_pos[i][1])
    black_res = max(black_res, dfs(black_pos, [black_pos[i]], i, used_right_diag, used_left_diag))

for i in range(len(white_pos)):
    used_right_diag = set()
    used_left_diag = set()

    used_right_diag.add(white_pos[i][0] + white_pos[i][1])
    used_left_diag.add(white_pos[i][0] - white_pos[i][1])
    white_res = max(white_res, dfs(white_pos, [white_pos[i]], i, used_right_diag, used_left_diag))

print(black_res + white_res)

# 이 문제는 그냥 전체로 풀면 시간초과가 뜬다.
# 흑, 백 나눠서 DFS를 진행하고 각각 MAX값을 더한게 답이 된다. <- 핵심