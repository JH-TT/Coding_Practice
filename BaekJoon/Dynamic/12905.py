def solution(board):
    answer = 0
    
    for i in range(len(board)-1):
        for j in range(len(board[0])-1):
            if board[i][j] == 0:
                continue
            if board[i][j] * board[i][j+1] * board[i+1][j] * board[i+1][j+1] > 0:
                board[i+1][j+1] = min(board[i][j], board[i+1][j], board[i][j+1]) + 1
                
    for i in board:
        answer = max(answer, max(i))
    
    
    return answer ** 2
