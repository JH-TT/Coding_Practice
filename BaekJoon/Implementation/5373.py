def up(t, idx):
    # 시계 방향 : 주 -> 파 -> 빨 -> 초 -> 주
    # 반시계 방향 : 주 -> 초 -> 빨 -> 파 -> 주
    start = orange[idx]
    if t == "+":
        start, blue[idx] = blue[idx], start
        start, red[idx] = red[idx], start
        start, green[idx] = green[idx], start
        start, orange[idx] = orange[idx], start
    else:
        start, green[idx] = green[idx], start
        start, red[idx] = red[idx], start
        start, blue[idx] = blue[idx], start
        start, orange[idx] = orange[idx], start

def down(t):
    # 시계 방향 : 주 -> 초 -> 빨 -> 파 -> 주
    # 반시계 방향 : 주 -> 파 -> 빨 -> 초 -> 주
    if t == "+":
        up("-", 2)
    else:
        up("+", 2)

def front(t, idx):
    # 시계 방향 : 흰 -> 파 -> 노 -> 초 -> 흰
    # 반시계 방향 : 흰 -> 초 -> 노 -> 파 -> 흰
    if t == "+":
        white[2-idx][0], blue[0][idx] = blue[0][idx], white[2-idx][0]
        white[2-idx][0], yellow[idx][2] = yellow[idx][2], white[2-idx][0]
        white[2-idx][0], green[2][2-idx] = green[2][2-idx], white[2-idx][0]

        white[2-idx][1], blue[1][idx] = blue[1][idx], white[2-idx][1]
        white[2-idx][1], yellow[idx][1] = yellow[idx][1], white[2-idx][1]
        white[2-idx][1], green[1][2-idx] = green[1][2-idx], white[2-idx][1]

        white[2-idx][2], blue[2][idx] = blue[2][idx], white[2-idx][2]
        white[2-idx][2], yellow[idx][0] = yellow[idx][0], white[2-idx][2]
        white[2-idx][2], green[0][2-idx] = green[0][2-idx], white[2-idx][2]
    else:
        white[2-idx][0], green[2][2-idx] = green[2][2-idx], white[2-idx][0]
        white[2-idx][0], yellow[idx][2] = yellow[idx][2], white[2-idx][0]
        white[2-idx][0], blue[0][idx] = blue[0][idx], white[2-idx][0]

        white[2-idx][1], green[1][2-idx] = green[1][2-idx], white[2-idx][1]
        white[2-idx][1], yellow[idx][1] = yellow[idx][1], white[2-idx][1]
        white[2-idx][1], blue[1][idx] = blue[1][idx], white[2-idx][1]

        white[2-idx][2], green[0][2-idx] = green[0][2-idx], white[2-idx][2]
        white[2-idx][2], yellow[idx][0] = yellow[idx][0], white[2-idx][2]
        white[2-idx][2], blue[2][idx] = blue[2][idx], white[2-idx][2]

def back(t):
    # front의 반대, 인덱스는 2
    if t == "+":
        front("-", 2)
    else:
        front("+", 2)

def left(t, idx):
    # 시계 방향 : 흰 -> 빨 -> 노 -> 주 -> 흰
    # 반시계 방향 : 흰 -> 주 -> 노 -> 빨 -> 흰
    if t == "+":
        white[0][idx], red[0][idx] = red[0][idx], white[0][idx]
        white[0][idx], yellow[0][idx] = yellow[0][idx], white[0][idx]
        white[0][idx], orange[2][2-idx] = orange[2][2-idx], white[0][idx]

        white[1][idx], red[1][idx] = red[1][idx], white[1][idx]
        white[1][idx], yellow[1][idx] = yellow[1][idx], white[1][idx]
        white[1][idx], orange[1][2-idx] = orange[1][2-idx], white[1][idx]

        white[2][idx], red[2][idx] = red[2][idx], white[2][idx]
        white[2][idx], yellow[2][idx] = yellow[2][idx], white[2][idx]
        white[2][idx], orange[0][2-idx] = orange[0][2-idx], white[2][idx]
    else:
        white[0][idx], orange[2][2-idx] = orange[2][2-idx], white[0][idx]
        white[0][idx], yellow[0][idx] = yellow[0][idx], white[0][idx]
        white[0][idx], red[0][idx] = red[0][idx], white[0][idx]

        white[1][idx], orange[1][2-idx] = orange[1][2-idx], white[1][idx]
        white[1][idx], yellow[1][idx] = yellow[1][idx], white[1][idx]
        white[1][idx], red[1][idx] = red[1][idx], white[1][idx]

        white[2][idx], orange[0][2-idx] = orange[0][2-idx], white[2][idx]
        white[2][idx], yellow[2][idx] = yellow[2][idx], white[2][idx]
        white[2][idx], red[2][idx] = red[2][idx], white[2][idx]

def right(t):
    if t == "+":
        left("-", 2)
    else:
        left("+", 2)

def clock(a):
    for x, y in clock_corner:
        a[0][0], a[x][y] = a[x][y], a[0][0]
    for x, y in clock_edge:
        a[0][1], a[x][y] = a[x][y], a[0][1]
    return a
    
def counterclock(a):
    for x, y in counterclock_corner:
        a[0][0], a[x][y] = a[x][y], a[0][0]
    for x, y in counterclock_edge:
        a[0][1], a[x][y] = a[x][y], a[0][1]
    return a

clock_corner = [[0, 2], [2, 2], [2, 0]]
clock_edge = [[1, 2], [2, 1], [1, 0]]
counterclock_corner = list(reversed(clock_corner))
counterclock_edge = list(reversed(clock_edge))

for _ in range(int(input())):
    white = [["w"] * 3 for _ in range(3)]
    red = [["r"] * 3 for _ in range(3)]
    blue = [["b"] * 3 for _ in range(3)]
    green = [["g"] * 3 for _ in range(3)]
    yellow = [["y"] * 3 for _ in range(3)]
    orange = [["o"] * 3 for _ in range(3)]
    
    m = int(input())
    for cmd in input().split():
        if cmd[0] == "L":
            left(cmd[1], 0)
            if cmd[1] == "+":
                green = clock(green)
            else:
                green = counterclock(green)
        elif cmd[0] == "R":
            right(cmd[1])
            if cmd[1] == "+":
                blue = clock(blue)
            else:
                blue = counterclock(blue)
        elif cmd[0] == "F":
            front(cmd[1], 0)
            if cmd[1] == "+":
                red = clock(red)
            else:
                red = counterclock(red)
        elif cmd[0] == "B":
            back(cmd[1])
            if cmd[1] == "+":
                orange = clock(orange)
            else:
                orange = counterclock(orange)
        elif cmd[0] == "U":
            up(cmd[1], 0)
            if cmd[1] == "+":
                white = clock(white)
            else:
                white = counterclock(white)
        else:
            down(cmd[1])
            if cmd[1] == "+":
                yellow = clock(yellow)
            else:
                yellow = counterclock(yellow)
    for w in white:
        print("".join(w))


# L과 R, F와 B, U와 D가 서로 반대라서 둘 중에 하나만 구현하고 나머지 하나는 다른 하나를 호출하는 방식으로 하면 됨