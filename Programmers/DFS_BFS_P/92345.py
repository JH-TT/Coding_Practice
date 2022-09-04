from collections import defaultdict

def solution(board, aloc, bloc):
    cor = defaultdict(list)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 1 -> 'a', -1 -> 'b'
    cor[1] = aloc
    cor[-1] = bloc
    
    # 범위를 벗어났는지 체크
    def check(x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return True
        return False
    
    def dfs(board2, player, cor):
        p_x, p_y = cor[player][0], cor[player][1]
        res = []
        # 다른 말이 움직여서 현재 위치가 0이 되면 종료
        if board2[p_x][p_y] == 0:
            return False, 0
        if board2[cor[-player][0]][cor[-player][1]] == 0:
            return True, 0
        
        for i in range(4):
            nx = p_x + dx[i]
            ny = p_y + dy[i]
          
            if check(nx, ny):
                continue
              
            if board2[nx][ny] == 1:
                board2[p_x][p_y] = 0
                cor[player] = [nx, ny]
                win, game_len = dfs(board2, player * (-1), cor)
                board2[p_x][p_y] = 1
                cor[player] = [p_x, p_y]
                res.append((not win, game_len + 1))
              
        if len(res) == 0:
            return False, 0
        elif any(r[0] for r in res):
            return True, min(r[1] for r in res if r[0])
        else:
            return False, max(r[1] for r in res)
          
    return dfs(board, 1, cor)[1]

# 참고 : https://velog.io/@dksung/programmer1
# 참고2 : https://school.programmers.co.kr/questions/32399