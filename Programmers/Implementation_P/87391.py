def solution(n, m, x, y, queries):
    answer = -1
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    x1, y1, x2, y2 = x, y, x, y
    # x : 행, y : 열
    for dir, cnt in queries[::-1]:
        # 열 이동
        # <- 방향
        if dir == 0:
            dir2 = 1 # 역추적 방향
            y2 = min(m-1, y2 + dy[dir2] * cnt) # 배열안에는 있도록 한다.
            # <- 방향에 벽이 있는지 확인
            if y1 != 0:
                y1 += dy[dir2] * cnt
        # -> 방향
        elif dir == 1:
            dir2 = 0
            y1 = max(0, y1 + dy[dir2] * cnt)
            # -> 방향에 벽이 있는지 확인
            if y2 != m-1:
                y2 += dy[dir2] * cnt
        # 위 방향
        elif dir == 2:
            dir2 = 3
            x2 = min(n-1, x2 + dx[dir2] * cnt)
            # 위 방향에 벽이 있는지 확인
            if x1 != 0:
                x1 += dx[dir2] * cnt
        else:
            dir2 = 2
            x1 = max(0, x1 + dx[dir2] * cnt)
            # 아래 방향에 벽이 있는지 확인
            if x2 != n-1:
                x2 += dx[dir2] * cnt
        # 범위를 벗어났다면 0리턴
        if x1 >= n or y1 >= m or x2 < 0 or y2 < 0:
            return 0
    return (x2 - x1 + 1) * (y2 - y1 + 1)

# 이 블로그와 프로그래머스 게시글을 확인하면 좋다
# https://deok2kim.tistory.com/348
# https://school.programmers.co.kr/questions/29706