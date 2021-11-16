import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 재귀 깊이 설정

def makeTree(current, p): # 트리생성 함수
    for node in graph[current]:
        if node != p:
            child[current].append(node)
            parent[node] = current
            makeTree(node, current)

def countSubtreeNodes(current): # 서브트리의 노드 개수 구하는 함수
    size[current] = 1 # 자기자신도 포함하므로 1로 시작.
    for node in child[current]:
        countSubtreeNodes(node)
        size[current] += size[node]

n, r, q = map(int, input().split()) # 노드개수, 루트노드, 쿼리수

graph = [[] for _ in range(n + 1)] # 모든 간선정보
parent = [x for x in range(n + 1)] # 각 노드의 부모노드
child = [[] for _ in range(n + 1)] # 각 노드의 자식노드들
size = [0 for _ in range(n + 1)] # 각 노드의 서브트리안에 노드 개수

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

makeTree(r, -1) # 루트노드는 부모노드가 -1
countSubtreeNodes(r) # 개수구하기 시작
for _ in range(q):
    print(size[int(input())])