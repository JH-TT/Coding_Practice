from collections import deque
import copy

n = int(input()) # 과목수
indegree = [0] * (n + 1) # 진입차수
graph = [[] for _ in range(n + 1)] # 각 노드에 연결된 간선 정보
time = [0] * (n + 1) # 각 강의 시간

for i in range(1, n + 1):
    data = map(int, input().split())
    time[i] = data[0] # 시간 정보 담는다.
    for x in data[1:-1]: # -1제외한 나머지 원소들
        indegree[i] += 1 # 노드 i의 진입차수 1추가.
        graph[x].append(i) # x의 선수강의.

def topology_sort():
    res = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0: # 진입차수가 0인것들을 q에 넣는다.
            q.append(i)
    while q:
        now = q.popleft() # 현재노드
        for i in graph[now]: # 그 노드의 선수과목들을 확인한다.
            res[i] = max(res[i], res[now] + time[i]) # 선수강의 i의 시간, 현재 과목의 걸리는 시간 + 선수강의 i의 원래 시간 중에 더 큰 값을 res[i]로 초기화.
            indegree[i] -= 1 # 진입차수 1뺌.
            if indegree[i] == 0: #진입차수가 0이 되면 q에 넣는다
                q.append(i)

    for i in range(1, n + 1):
        print(res[i])

topology()

# 각 강의를 수강하기까지의 최소 시간을 res에 담음.