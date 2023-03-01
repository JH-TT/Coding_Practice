def solution(board):
    board = [list(board[i]) for i in range(3)]
    o, o_success = 0, 0
    x, x_success = 0, 0
    # X, O의 개수 확인 겸 가로줄 완성 확인
    for i in range(3):
        sub_o = 0
        sub_x = 0
        for j in range(3):
            if board[i][j] == "O":
                o += 1
                sub_o += 1
            elif board[i][j] == "X":
                x += 1
                sub_x += 1
        if sub_o == 3:
            o_success += 1
        elif sub_x == 3:
            x_success += 1
    # 세로 확인
    for i in range(3):
        sub_board = board[0][i] + board[1][i] + board[2][i]
        if len(set(sub_board)) != 1:
            continue
        if sub_board[0] == "O":
            o_success += 1
        if sub_board[0] == "X":
            x_success += 1
    # 대각선 확인
    sub_board1 = board[0][0] + board[1][1] + board[2][2]
    sub_board2 = board[0][2] + board[1][1] + board[2][0]
    if len(set(sub_board1)) == 1:
        if sub_board1[0] == "O":
            o_success += 1
        if sub_board1[0] == "X":
            x_success += 1
    if len(set(sub_board2)) == 1:
        if sub_board2[0] == "O":
            o_success += 1
        if sub_board2[0] == "X":
            x_success += 1

    # 아예 처음 시작상태(o, x 둘 다 없음)는 무조건 1
    if x + o == 0:
        return 1
    # 개수로만 따지면 x의 개수는 o의 개수보다 많으면 안된다.
    if x > o:
        return 0
    # o의 개수는 x의 개수보다 아무리 더 많아봐야 1개까지이다.
    if o - x > 1:
        return 0
    
    # 1줄 완성은 O또는 X 둘 중 하나만 있어야 한다.
    if o_success > 0 and x_success > 0:
        return 0
    
    # O의 개수가 더 많은데 x가 이미 완성된 곳이 있으면 안된다.
    # O와 X의 개수가 같은데 O가 이미 완성돼 있으면 안된다.
    if o == x and o_success == 1:
        return 0
    if o > x and x_success == 1:
        return 0
    
    return 1

# 그냥 구현
# 안되는 조건을 생각하는게 더 오래걸렸다.