# 메모이제이션 X
# for문 마다 측정해야할 수도

import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lights = sorted(list(map(int, input().split())))
ran = []

sb = [] # 현재 범위
for i in range(1, n):
    a = lights[i]   # 현재 가로등
    b = lights[i-1] # 이전 가로등
    # 만약 겹치는지 안겹치는지 확인한다.
    if a-l <= b+l:
        # sb가 없으면 새롭게 만들어 준다.
        if not sb:
            sb = [a-l, b+l]
            continue
        # sb가 있으면 겹치는 범위를 확인한다.
        # 1. 겹치는 최대 좌표가 a-l보다 이전에 있으면 기존 범위는 넣고, 새로운 sb범위를 만든다.
        # 2. 그대로 겹치면 새로운 범위를 업데이트 한다.
        if sb[1] < a-l:
            ran.append(sb)
            sb = [a-l, b+l]
        else:
            sb = [sb[0], b+l]
    else:
        ran.append(sb)
        sb = []
ran.append(sb)

sum = 0
for i in ran:
    if not i:
        continue
    sum += (i[1] - i[0])
print(sum)

# 새로 겹치는 범위를 업데이트 하는 방식으로 한다.
# 만약 현재 겹치는 범위가 -5 ~ -2 이고 다른 겹치는 범위가 -3 ~ 1 이면 기존으로부터 새로 생시는 범위는 -1~1 이므로 -5 ~ 1로 업데이트 하는 방식으로 한다.