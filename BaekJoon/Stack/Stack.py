# 큐랑 다른점은 큐는 먼저 들어간게 먼저 나오지만
# 스택은 먼저 들어간게 가장 마지막으로 나온다.
import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
    c = list(input().split())
    if c[0] == "push":
        s.append(c[1])
    elif c[0] == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop()) # 마지막으로 들어간게 나오는거니 뒤에서부터 뺀다.(큐와의 큰 차이점)
    elif c[0] == "size":
        print(len(s))
    elif c[0] == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])