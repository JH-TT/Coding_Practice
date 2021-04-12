from collections import deque

n, k = map(int, input().split())
q = deque(x for x in range(1, n + 1))
count = 0

print("<", end="")
while len(q) != 1: # 큐가 빌때까지
    sub = deque()
    while q and count != k:
        sub.append(q.popleft())
        count += 1
    if count != k: # q가 비었다면
        q += sub # sub에 있는 배열을 q 뒤로 옮긴다.
    elif count == k: # k번째 사람이라면
        print(sub.pop(), end=", ") # 뽑고, sub에 있는 배열을 q 뒤로 옮긴다.
        q += sub
        count = 0 # count를 0으로 초기화한다.

print(q[0], end=">")