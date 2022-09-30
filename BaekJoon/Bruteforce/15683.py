from itertools import combinations

def check(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False
    return True

def add_case(a, b, case):
    c = []
    if arr[a][b] == 1:
        c += case # 이 부분만 + 인 이유는 case자체가 모든 경우의 수가 되기때문에 따로 리스트에 담아서 할 필요가 없다.
    elif arr[a][b] == 2:
        c.append(case[0] + case[1])
        c.append(case[2] + case[3])
    elif arr[a][b] == 3:
        c.append(case[0]+case[3])
        c.append(case[0]+case[2])
        c.append(case[1]+case[3])
        c.append(case[1]+case[2])
    elif arr[a][b] == 4:
        c.append(case[0]+case[1]+case[2])
        c.append(case[0]+case[1]+case[3])
        c.append(case[0]+case[2]+case[3])
        c.append(case[1]+case[2]+case[3])
    elif arr[a][b] == 5:
        c.append(case[0]+case[1]+case[2]+case[3])
    all_case.append(c)

def dfs(track, idx):
    global res
    if idx == len(all_case):
        # print(track)
        res = min(res, n*m - len(set(track)) - cnt)
        return
    # print(all_case[idx])
    # print()
    for i in all_case[idx]:
        arr = []
        for j in i:
            # print(j)
            arr.append(j)
        # print(arr)
        dfs(track + arr, idx+1)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

global res
res = float('inf')
all_case = []
cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0:
            cnt += 1
        if arr[i][j] in [1, 2, 3, 4, 5]:
            case = []
            for h in range(4):
                c = []
                x, y = i + dx[h], j + dy[h]
                while check(x, y):
                    if arr[x][y] == 0:
                        c.append((x, y))
                    if arr[x][y] == 6:
                        break
                    x += dx[h]
                    y += dy[h]
                case.append(c)
            add_case(i, j, case)
# print(len(all_case))
# print(all_case)
dfs([], 0)
print(res)

# 모든 경우를 구한 방식
# 각 cctv가 볼 수 있는 4방향을 구한다.
# cctv번호에 맞게 동서남북 시야 범위 구한 리스트를 잘 조합한다. -> add_case부분.
# 재귀를 이용해서 백트래킹돌린다.