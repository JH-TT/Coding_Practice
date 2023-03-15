def solution(n):
    answer = 0
    for i in range(2, n+1):
        if (n-1) % i == 0:
            return i
# 그냥 선형탐색으로 찾는다