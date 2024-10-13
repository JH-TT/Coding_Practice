from collections import deque
import sys
input = sys.stdin.readline

cmd = []
q = deque()

for _ in range(int(input())):
    btn = input().split()
    c = int(btn[0])
    if c == 1:
        cmd.append(c)
        q.append(btn[1])
    elif c == 2:
        cmd.append(c)
        q.appendleft(btn[1])
    else:
        if not cmd or not q:
            continue
        last = cmd.pop()
        if last == 1:
            q.pop()
        else:
            q.popleft()
print("".join(q) if q else 0)

# 문제 조건에 따라 맞게 구현하면 되는 문제