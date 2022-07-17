import sys
input = sys.stdin.readline


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1-x2)**2 + (y1-y2)**2) ** (0.5)
    if int(d) == d:
        d = int(d)
    R = max(r1, r2)
    r = min(r1, r2)

    # 일단 크게 중심이 같을때와 다를때로 나눠진다.
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if d > R + r:
            print(0)
        elif d == R + r:
            print(1)
        elif R-r < d < R+r:
            print(2)
        elif d == R-r:
            print(1)
        elif d < R-r:
            print(0)

# 두 원의 위치에 따른 교점 개수에 대한 문제.
# 크게 중심이 같을때와 다를떄로 나누고
# 중심이 같으면 반지름만 비교해서 출력하고
# 다르면 두 원의 반지름길이 + 중심거리를 이용해서 개수를 출력한다.