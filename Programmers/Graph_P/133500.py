import sys
sys.setrecursionlimit(10**7)

def solution(n, lighthouse):
    
    def dfs(node, flag):
        global cnt
        if ind[node] == 1:
            return False
        visit[node] = 1
        for next in graph[node]:
            if visit[next]:
               continue
            v = dfs(next, False)
            light[node] = light[node] or (not v) # 이미 켜진 등대거나 인접한 등대가 꺼진 경우 현재 등대는 불이 켜져야 한다.
        
        if light[node] and not flag: # 시작 노드가 아닌 경우는 cnt를 증가시킨다.(시작 노드는 dfs전에 증가시켰기 때문)
            cnt += 1
        return light[node]
        
    graph = [[] for _ in range(n+1)]
    ind = [0] * (n + 1)
    
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
        ind[a] += 1
        ind[b] += 1
    
    visit = [0] * (n + 1)
    light = [False] * (n + 1)
    for i in range(1, n+1):
        if any(ind[x] == 1 for x in graph[i]):
            start = i
            break
    global cnt
    cnt = 1
    dfs(start, True)
    return cnt

# 2가지를 유의하고 풀어야 했다.
# 1. 리프노드는 항상 불이 꺼져야 한다.
# 2. 만약 근접한 등대가 꺼져있으면 현재 등대는 반드시 켜져야 한다. (한 뱃길의 양쪽 끝 등대 중 적어도 하나는 켜져 있도록 등대를 켜 두어야 합니다. -> 문제에 있던 조건)
# A ---- B 이렇게 등대가 있으면 A 혹은 B 둘 중 하나는 반드시 등대가 켜져야 한다는 것이다.
# 이는 A - B - C - D - E - F 를 생각해 보면 B, E는 반드시 키게되는데 사실 그냥 두면 전부 길이 밝혀져서 되는것 같지만
# 2번의 조건때문에 C 혹은 D 둘 중 하나는 켜야한다. 따라서 위의 예시는 답이 3개가 된다.