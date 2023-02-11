from collections import defaultdict

def dfs(node):
    # -1노드는 내가 따로 만든 노드이기 때문에 -1노드와 연결된 노드가 없으면 아예 노드들이 없다고 판단한다.
    if len(graph[node]) == 0 and node != -1:
        return 1
    total = 0
    for i in graph[node]:
        total += dfs(i)
    return total

n = int(input())
nodes = list(map(int, input().split()))
k = int(input())
graph = defaultdict(list) # 루트노드의 루트노드를 선언하기위해 딕셔너리를 사용한다. (조상노드 -1을 만들기 위함)

for i in range(n):
    # 그래프를 만들때 삭제할 노드인 경우는 건너뛴다.
    # 해당 노드만 지워줘도 그 아래노드는 갈 방법이 없어지기 때문에 함께 삭제된 상태와 같다고 볼 수 있다.
    if i == k:
        continue
    graph[nodes[i]].append(i)
print(dfs(-1))