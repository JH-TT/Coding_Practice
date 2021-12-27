from collections import deque


def solution(game_board, table):
    game_board = [list(map(lambda z : (z + 1) % 2, x)) for x in game_board] # 1과 0을 바꿔준다.

    # 퍼즐의 좌표 정보를 얻는 함수.
    def bfs(puzzle, a, b):
        q = deque()        
        q.append([a, b])
        cor = [[a, b]]
        puzzle[a][b] = 0
        min_x, min_y = a, b
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx >= len(puzzle) or ny < 0 or ny >= len(puzzle):
                    continue
                
                if puzzle[nx][ny] == 1:
                    cor.append([nx, ny])
                    puzzle[nx][ny] = 0
                    q.append([nx, ny])
                    min_x = min(min_x, nx)
                    min_y = min(min_y, ny)
        cor = list(map(lambda x : (x[0] - min_x, x[1] - min_y), cor)) # (0, 0)에 맞추기 위함.

        return cor
    
    # 90도 회전
    def spin(_cor):
        max_n = 0
        min_x = len(_cor) - 1
        min_y = len(_cor) - 1
        for i in _cor:
            max_n = max(max_n, i[0], i[1])            
        _cor = list(map(lambda x : (x[1], max_n - x[0]), _cor))
        
        # 회전 시켜주고 다시 (0, 0)에 맞춰준다.
        for i in _cor:
            min_x = min(min_x, i[0])        
            min_y = min(min_y, i[1])
                
        _cor = list(map(lambda x : (x[0]-min_x, x[1]-min_y), _cor))

        return _cor
    
    
    answer = 0
    puzzle_cor = []
    puzzle_game = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == 1:
                puzzle_cor.append(bfs(table, i, j))
    
    for i in range(len(game_board)):
        for j in range(len(game_board)):
            if game_board[i][j] == 1:
                puzzle_game.append(bfs(game_board, i, j))

    # 비교
    for g in puzzle_game:      
        for t in puzzle_cor:            
            flag = False # 찾으면 바로 다음꺼 확인.
            g.sort()
            T = t
            for _ in range(4):
                T.sort()
                if len(g) != len(T):
                    break
                if g == T:  
                    answer += len(T)
                    flag = True
                    puzzle_cor.remove(t)
                    break
                else:
                    T = spin(T)
            if flag:
                break                
    
    return answer