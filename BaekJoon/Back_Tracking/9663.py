n = int(input())
row = [0] * n

def isvalid(x):
    for i in range(x):
        # 퀸을 놓을 수 없는지의 여부. 왼쪽은 같은 열인지 확인, 오른쪽은 다른 퀸의 대각선위치에 있는지 확인.
        if row[i] == row[x] or abs(row[i] - row[x]) == abs(i - x):
            return False
          
    return True

def dfs(x):
    global cnt
    if x == n:
        # 퀸을 다 채우면 cnt증가.
        cnt += 1
        return
    for i in range(n):
        # [x, i]에 퀸을 놓았다는 의미.
        row[x] = i
        if isvalid(x):
            dfs(x + 1)
global cnt
cnt = 0
dfs(0)
print(cnt)