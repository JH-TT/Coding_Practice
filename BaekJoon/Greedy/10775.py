from collections import defaultdict

g = int(input())
p = int(input())

check = defaultdict(int) # 현재 key에 대한 남은자리중 가장 높은 인덱스
for i in range(1, g + 1):
    check[i] = i
visited = [False for _ in range(g + 1)]
cnt = 0
for _ in range(p):
    a = int(input())
    idx = check[a]
    flag = False
    while idx > 0:
        if not visited[idx]:
            visited[idx] = True
            cnt += 1
            check[a] = idx - 1 # 다음 인덱스를 저장한다.
            flag = True
            break
        idx -= 1
    if not flag:
        break
print(cnt)

# union사용해서 경로압축해 풀기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    px = find_parent(parent, x)
    py = find_parent(parent, y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

g = int(input())
p = int(input())

parent = [i for i in range(g + 1)]
cnt = 0

for _ in range(p):
    n = int(input())
    np = find_parent(parent, n)
    if np == 0:
        break
    union_parent(parent, np, np - 1)
    cnt += 1
print(cnt)