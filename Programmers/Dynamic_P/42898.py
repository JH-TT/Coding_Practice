def solution(m, n, puddles):
    v = [[-1] * (m + 1) for _ in range(n + 1)]
    
    # 오른쪽, 아래만 움직인다고 함.
    dx = [1, 0]
    dy = [0, 1]
    
    def dfs(x, y):
        if x == n and y == m: # 끝 지점이면 1 리턴.
            return 1
        if v[x][y] != -1: # 이미 지난 곳 이면 다시 그대로 리턴.
            return v[x][y]
        v[x][y] = 0 # 처음 온 곳이면 일단 0으로 초기화.
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            if [ny, nx] in puddles: # 웅덩이면 넘김.
                continue
            v[x][y] += dfs(nx, ny) # 재귀 실행.
        
        return v[x][y]
    answer = dfs(1, 1)
    
    return answer % 1000000007
