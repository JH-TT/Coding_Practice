import heapq
import sys
input = sys.stdin.readline

def find(p, x): # 부모노드 찾기
    if p[x] != x: # 자기자신이 부모노드가 아니면 재귀함수를 돈다.
        p[x] = find(p, p[x])
    return p[x]

def union(arr, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b: # 둘 중에 더 작은값을 부모노드로 지정.
        p[b] = a
    else:
        p[a] = b

n = int(input()) # 노드 개수
m = int(input()) # 간선 개수

p = [0] + [i for i in range(1, n + 1)] # 부모노드 기본값
arr = [] # 각 노드들끼리의 정보를 넣을 공간.
res = 0

for _ in range(m):
    a, b, c = map(int, input().split()) 
    arr.append((c, a, b)) # 비용을 기준으로 정렬하기 위해 비용을 가장 앞에 둔다.
arr.sort()

for c, a, b in arr:
    if find(p, a) != find(p, b): # 서로 부모노드가 다르면 같은 집합에 있지 않다는 의미!
        union(p, a, b) # 합쳐준다.
        res += c # 그 비용을 더해준다
print(res)
