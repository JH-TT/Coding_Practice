import sys
input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split())

    # 둘의 차이가 1이면 1만 출력하고 넘긴다.
    if y - x == 1:
        print(1)
        continue

    # 여기부턴 2이상의 영역
    dist = y - x
    left, right, move = 1, 1, 1
    while True:
        rest = dist - move * (move + 1)
        if rest <= 0:
            print(move * 2)
            break

        if rest <= move + 1:
            print(move * 2 + 1)
            break

        move += 1

# 그냥 규칙을 찾아서 푸는 문제