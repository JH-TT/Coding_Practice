import copy
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip() # 엔터키를 제거하기 위함.
    n = int(input())
    # num = list(input().rstrip("]").lstrip("[").split(","))
    num = input().rstrip()[1:-1].split(",") # 엔터키 제거, 왼쪽과 오른쪽 대괄호를 빼고, ","를 기준으로 나눈다.
    num = deque(num)
    if p.count("D") > n:
        print("error")
        continue
    # 아래 while문은 R이 연속으로 2번나오면 그대로 둔 것과 같으므로 replace함수를 이용해 RR을 ""로 바꿔주는것을 해 놓음. 근데 밑에 flag때문에 궅이 안해도 될듯.
    # while 1:
    #     h = p.replace("RR", "")
    #     if h == p:
    #         break
    #     p = copy.deepcopy(h)
    
    flag = 1 # 뒤집었는지 안뒤집었는지 확인. 1이면 그대로 -1이면 뒤집음
    for i in p:
        if i == "R":
            flag *= -1
        elif i == "D":
            if flag == 1:
                num.popleft()
            elif flag == -1:
                num.pop()
    if flag == -1:
        num.reverse()
    print("[" + ','.join(num) + "]")

# 처음에는 리스트로 했는데 풀이는 맞았으나 시간이 3000ms나 걸렸다.
# deque로 다시푸니 시간이 300ms대로 확 줄었으나 메모리는 리스트로만 했을때 보단 더 많이 사용함.
# 어쩔땐 그냥 리스트가 빠를때도 있고, 어쩔땐 deque가 더 빠를때도 있는데 보통은 deque가 빠른편인듯 하다.