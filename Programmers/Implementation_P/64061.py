def solution(board, moves):
    answer = 0
    stack = []
    loc = {}
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[j][i] != 0:
                loc[i+1] = j
                break
    
    for m in moves:
        if loc[m] == len(board):
            continue
        v = board[loc[m]][m-1]
        loc[m] += 1
        if not stack or stack[-1] != v:
            stack.append(v)
        elif stack[-1] == v:
            stack.pop()
            answer += 2
        
    return answer