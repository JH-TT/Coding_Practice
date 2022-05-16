# 나간 방향에 따라 좌표변경
def select_direct(a, b, n, r, c) -> list:
    if n == 0:
        return [(a - 1) % r, b]
    elif n == 1:
        return [a, (b + 1) % c]
    elif n == 2:
        return [(a + 1) % r, b]
    else:
        return [a, (b - 1) % c]

def solution(grid):
    answer = []
    col = len(grid[0])
    row = len(grid)
    
    # (a, b)좌표에서 4방향리스트 0 : up, 1 : right, 2 : down, 3 : left
    node = [[[0 for _ in range(4)] for _ in range(col)] for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            for h in range(4):
                cnt = 1
                node[i][j][h] = 1

                a, b = select_direct(i, j, h, row, col) # 현재 노드좌표
                c = h # 빛의 방향

                while 1:
                    # "S"는 방향이 그대로이므로 L이랑 R만 추가한다.
                    # L이면 빛의 방향기준 반시계방향이니 인덱스를 1 감소.
                    # R이면 반대.
                    # 범위안에서 돌아야하므로 % 사용.
                    if grid[a][b] == "L":
                        c = (c - 1) % 4
                    elif grid[a][b] == "R":
                        c = (c + 1) % 4
                    
                    # 왔던곳이면 반복문 탈출.
                    if node[a][b][c] == 1:
                        break

                    cnt += 1
                    node[a][b][c] = 1

                    a, b = select_direct(a, b, c, row, col)
                    
                # 반복문을 빠져나왔는데 처음 시작한 노드이자 방향이면 새로운 사이클로 간주함.
                # 중간에 겹치는 사이클이 없었다는 소리.
                if a == i and b == j and c == h:                    
                    answer.append(cnt)    
                
    return sorted(answer)