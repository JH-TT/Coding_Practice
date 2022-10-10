dx = [-1, 0, 1]

def dfs(x, y):
    # 빵집에 도착하면 1리턴.
    # 여기서 1이 리턴되면 처음 부분까지 전부 1로 리턴될 것이다.
    if y == C-1:
        return 1
      
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if arr[nx][ny] == "." and not visit[nx][ny]:
            visit[nx][ny] = 1
            if dfs(nx, ny):
                return 1
    return 0

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]
visit = [[0 for _ in range(C)] for _ in range(R)]

res = 0
for i in range(R):
    if arr[i][0] == "x":
        continue
    res += dfs(i, 0) # 리턴값이 0 or 1이니 그냥 바로 더해준다.
print(res)

# 이 문제는 오른쪽위, 오른쪽, 오른쪽아래 순으로 가는것이 포인트였다.
# 나는 포인트 부분까진 바로 알아차렸지만, 다음에 그래프 탐색을 하다가 빵집에 도착하면 바로 다음 가스로 넘어가는 부분을 구현하는 데에 좀 생각을 많이 했다.


# 좀 더 깔끔한 코드
# 불필요한 visit을 지웠다.
dx = [-1, 0, 1]

def dfs(x, y):
    
    if y == C-1:
        return 1
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if arr[nx][ny] == ".":
            arr[nx][ny] = "x" # 어차피 arr이 x이냐 .이냐만 따지니까 굳이 visit을 넣을 필요는 없다. 그러니 방문처리를 x로 한다.
            if dfs(nx, ny):
                return 1
    return 0

R, C = map(int, input().split())

arr = [list(input()) for _ in range(R)]

res = 0
for i in range(R):
    if arr[i][0] == "x":
        continue
    res += dfs(i, 0)
print(res)