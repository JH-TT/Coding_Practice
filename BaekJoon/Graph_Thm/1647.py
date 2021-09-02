# 특정 원소가 속한 집합 찾기
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: # 더 작은 값을 기준으로 합침.
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = list(range(n + 1))

edge = [] # 비용, 두 도시 의 정보를 입력받을 공간.
res = 0 # 총 비용

for i in range(m):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))

edge.sort() # 비용순으로 정렬
m_cost = 0
for i in edge:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += c
        m_cost = max(m_cost, c)
print(res - m_cost)