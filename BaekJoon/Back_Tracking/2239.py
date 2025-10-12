# 3x3에서 숫자 체크
def check3By3(arr, num, i, j):
    w_i = i // 3
    w_j = j // 3
    for k in range(3 * w_i, 3 * (w_i + 1)):
        for h in range(3 * w_j, 3 * (w_j + 1)):
            if arr[k][h] == num:
                return False
    return True

# 가로줄 숫자 체크
def holizontalCheck(arr, num, i):
    for j in range(9):
        if arr[i][j] == num:
            return False
    return True

# 세로줄 숫자 체크
def verticalCheck(arr, num, j):
    for i in range(9):
        if arr[i][j] == num:
            return False
    return True

def validation(arr, num, i, j):
    return check3By3(arr, num, i, j) and holizontalCheck(arr, num, i) and verticalCheck(arr, num, j)

def dfs(arr, i, j):
    for n in range(1, 10):
        if validation(arr, n, i, j):
            arr[i][j] = n
            n_i = -1
            n_j = -1
            for k in range(9):
                dfs_flag = False
                for h in range(9):
                    if arr[k][h] == 0:
                        n_i = k
                        n_j = h
                        dfs_flag = True
                        break
                if dfs_flag:
                    break
            # 마지막인 경우 출력한다.
            if n_i == -1 and n_j == -1:
                for a in arr:
                    print(''.join(map(str, a)))
                exit(0)
            dfs(arr, n_i, n_j)
            arr[i][j] = 0

arr = [list(map(int, input())) for i in range(9)]

s_i = -1
s_j = -1
for i in range(9):
    flag = False
    for j in range(9):
        if arr[i][j] == 0:
            s_i = i
            s_j = j
            flag = True
            break
    if flag:
        break
# 만약 처음부터 0이 없고 완성된 형태로 주어진다면 그대로 출력한다.
if s_i == -1 and s_j == -1:
    for a in arr:
        print(''.join(map(str, a)))
else:
    dfs(arr, s_i, s_j)

# 일반적인 백트래킹 문제
# 그냥 보면 쉬워보이지만 막상 할 때 바로 구현하기가 쉽지 않았던 문제.
# 그래도 핵심만 확인되면 금방 해결된 문제였음.