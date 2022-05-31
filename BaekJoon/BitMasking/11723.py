import sys
input = sys.stdin.readline

m = int(input())
s = 0
for _ in range(m):
    a = list(input().split())
    if a[0] == "add":
        s |= (1 << int(a[1]))
    elif a[0] == "remove":
        s &= ~(1 << int(a[1]))
    elif a[0] == "check":
        print(1 if s & (1 << int(a[1])) != 0 else 0)
    elif a[0] == "toggle":
        s ^= (1 << int(a[1]))
    elif a[0] == "all":
        s = (1 << 21) - 1
    else:
        s = 0


# 집합에서 비트마스킹이 어떤식으로 쓰이는지 잘 보여주는 문제.