def check(sudoku, a, b):
    visit = [0 for _ in range(10)]

    able = []
    # 하나의 for문으로 가로, 세로, 3x3을 다 확인한다.
    for i in range(9):
        visit[sudoku[a][i]] += 1
        visit[sudoku[i][b]] += 1
        visit[sudoku[3 * (a // 3) + (i // 3)][3 * (b // 3) + (i % 3)]] += 1

    for i in range(1, 10):
        # visit값이 0이면 들어갈수 있는 숫자이다.
        if visit[i] == 0:
            able.append(i)

    return able

def print_sudoku(sudoku):
    for s in sudoku:
        print(*s)

# 스도쿠 특징상 각 위치마다 숫자들이 정해져(?) 있다보니 0인 좌표 인덱스(여기서 zero)를 순서대로 확인해도 무방하다
def dfs(sudoku, zero, idx):
    x, y = zero[idx]
    possible = check(sudoku, x, y)

    for p in possible:
        sudoku[x][y] = p
        if idx == len(zero) - 1: # 마지막 좌표면 완성되었기 때문에 출력하고 종료한다.
            print_sudoku(sudoku)
            exit() # 완성되면 강제 종료시킨다.
        dfs(sudoku, zero, idx + 1) # 다음 0좌표
    sudoku[x][y] = 0

sudoku = []
zero = [] # 값이 0인 좌표
for i in range(9):
    line = list(map(int, input().split()))
    sub = []
    for j in range(9):
        if line[j] == 0:
            zero.append((i, j))
        sub.append(line[j])
    sudoku.append(sub)

# dfs(스도쿠 상태, 값이 0인 좌표 리스트, 현재 zero 인덱스)
dfs(sudoku, zero, 0)
