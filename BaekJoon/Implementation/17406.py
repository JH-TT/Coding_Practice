import sys, copy
from itertools import permutations
input = sys.stdin.readline

def spin_arr(a, b, h, arr3):
    a -= h
    b -= h
    data = arr3[a][b]
    # -> 방향
    for i in range(2*h):
        arr3[a][b+i+1], data = data, arr3[a][b+i+1]
    b += 2*h
    # 아래 방향
    for i in range(2*h):
        arr3[a+i+1][b], data = data, arr3[a+i+1][b]
    a += 2*h
    # <- 방향
    for i in range(2*h):
        arr3[a][b-i-1], data = data, arr3[a][b-i-1]
    b -= 2*h
    # 위 방향
    for i in range(2*h):
        arr3[a-i-1][b], data = data, arr3[a-i-1][b]

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = sys.maxsize
cases = [list(map(int, input().split())) for _ in range(k)]

for case in permutations(cases, k):
    arr2 = copy.deepcopy(arr)
    for c in case:
        a = c[0]-1
        b = c[1]-1
        for i in range(1, c[2]+1):
            spin_arr(a, b, i, arr2)
    res = min(res, min(sum(x) for x in arr2))
print(res)

# 잘 나오는 배열 돌리기 문제
# 케이스가 적어서 완탐으로 돌아갔다