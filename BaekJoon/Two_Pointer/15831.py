from collections import deque

n, b, w = map(int, input().split())
stone = deque(list(input()))
road = deque() # 가져가는 돌

ans = 0
white = 0
black = 0

while stone:
    # 흰돌이면 white 검은 돌이면 black의 값을 1씩 더해준다.
    if stone[0] == "W":
        white += 1
    else:
        black += 1
    road.append(stone.popleft())
    # 만약 돌의 개수가 최대치를 넘으면 다시 조건이 만족될 때 까지 돌을 빼준다.
    if black > b:
        while black > b:
            a = road.popleft()
            if a == "W":
                white -= 1
            else:
                black -= 1
    # 흰돌 검은돌의 조건이 완료되면 ans와 흰돌+검은돌중에 큰 값을 ans로 둔다.
    if white >= w and black <= b:
        ans = max(ans, white + black)

print(ans)

# 처음엔 리스트로 pop(0)을 하니까 100점밖에 안됐는데
# deque를 이용하니 만점(250점)을 받았다.