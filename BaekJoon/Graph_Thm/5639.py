import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def postorder(s, e):
    if s > e:
        return
    idx = e
    for i in range(e, s, -1):
        if graph[i] < graph[s]:
            idx = i
            break
          
    postorder(s+1, idx)
    postorder(idx+1, e)
    print(graph[s])

graph = []

while 1:
    try:
        node = int(input())
        graph.append(node)
    except:
        break

postorder(0, len(graph)-1)

# s번째 인덱스가 루트 노드가 된다.
# s+1 부터 e까지 중에 루트노드값보다 커지는 순간 그 부분은 오른쪽 트리, 그 전은 왼쪽 트리
# 재귀이용