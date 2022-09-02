def solution(board, skill):
    answer = 0
    x = len(board)
    y = len(board[0])
    prefix_board = [[0] * (y + 1) for _ in range(x + 1)]
    for type, x1, y1, x2, y2, degree in skill:
        if type == 1:
            prefix_board[x1][y1] += -degree
            prefix_board[x1][y2+1] += degree
            prefix_board[x2+1][y1] += degree
            prefix_board[x2+1][y2+1] += -degree
        else:
            prefix_board[x1][y1] += degree
            prefix_board[x1][y2+1] += -degree
            prefix_board[x2+1][y1] += -degree
            prefix_board[x2+1][y2+1] += degree
    
    # 누적합 시작 (위 -> 아래)
    for i in range(y + 1):
        for j in range(1, x + 1):
            prefix_board[j][i] += prefix_board[j-1][i]
    # 누적합 시작 (왼쪽 -> 오른쪽)
    for i in range(x + 1):
        for j in range(1, y + 1):
            prefix_board[i][j] += prefix_board[i][j-1]
    # 마무리
    for i in range(x):
        for j in range(y):
            board[i][j] += prefix_board[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer

# 참고 : https://tech.kakao.com/2022/01/14/2022-kakao-recruitment-round-1/#%EB%AC%B8%EC%A0%9C-6-%ED%8C%8C%EA%B4%B4%EB%90%98%EC%A7%80-%EC%95%8A%EC%9D%80-%EA%B1%B4%EB%AC%BC