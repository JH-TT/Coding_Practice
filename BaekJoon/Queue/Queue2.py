# 알고리즘은 Queue.py랑 같음. 근데 이건 deque라이브러리를 이용해서 큐 구현.
# pop은 뒤를 popleft는 앞을 뽑는다.
# deque는 추가, 제거 시간복잡도가 O(1)이다.
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

array = deque()
for _ in range(n):
    c = list(input().split())
    if c[0] == "push":
        array.append(c[1])
    elif c[0] == "pop":
        if len(array) == 0:
            print(-1)
        else:
            print(array.popleft())
    elif c[0] == "size":
        print(len(array))
    elif c[0] == "empty":
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif c[0] == "front":
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
    elif c[0] == "back":
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])