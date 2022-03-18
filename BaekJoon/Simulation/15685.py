def check_square(cor):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if cor[i][j] == 1:
                # 세 부분의 합이 3이면 사각형을 이룬다는 것
                if cor[i+1][j] + cor[i][j+1] + cor[i+1][j+1] == 3:
                    cnt += 1
                  
    return cnt

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

graph = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    dragon_curve = [[x, y]]
    graph[y][x] = 1    

    # 0세대 이동
    nx = x + dx[d]
    ny = y + dy[d]
    graph[ny][nx] = 1
    dragon_curve.append([nx, ny])
  
    end_point = [nx, ny] # 끝점
    # 세대별 이동
    for _ in range(g):
        spinned = list(map(list, map(lambda x : (-x[1]+end_point[1]+end_point[0], x[0]-end_point[0]+end_point[1]), dragon_curve)))
        
        dragon_curve.extend(spinned) # 회전시킨 부분 추가
        dragon_curve.remove(end_point) # 끝점 중복 없애주기

        end_point = [-y+end_point[1]+end_point[0], x-end_point[0]+end_point[1]] # 끝점 갱신

    for cor in dragon_curve:
        graph[cor[1]][cor[0]] = 1

print(check_square(graph))

# 이 문제의 핵심은 90도 회전시 좌표의 변화와 끝점의 변화에 있었다
# 90도 회전시 (x, y)의 좌표는 (-y, x)로 바뀌고
# 끝점은 드래곤커브의 시작점이 작업을 거친 후 끝점이 된다