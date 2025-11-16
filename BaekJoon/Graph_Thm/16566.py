import sys
from bisect import bisect_right
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)

    if x < y:
        parent[x] = y
    else:
        parent[y] = x

m, n, k = map(int, input().split())
cards = sorted(list(map(int, input().split())))
cheolsu = list(map(int, input().split()))
parent = [i for i in range(m + 1)]

for c in cheolsu:
    idx = bisect_right(cards, c)
    pidx = find_parent(idx)
    print(cards[pidx])
    union_parent(pidx, pidx + 1)

# 이분탐색 + union_find
# 사용한 숫자는 더 이상 사용할 수 없기 때문에 바로바로 보여야할 인덱스를 찾아가야한다
# 따라서 union_find를 이용해서 현재 인덱스를 사용했으면 다음 인덱스와 union해서 같은 인덱스가 와도 다음 인덱스를 바로 찾아서 그 인덱스로 보이도록 한다.