import sys
sys.setrecursionlimit(10**6)

def solution(a, edges):    
    
    def dfs(n):
        global answer
        visit[n] = 1
        for i in edge[n]:
            if not visit[i]:
                c = dfs(i)
                a[n] += c
                answer += abs(c)
        return a[n]
        
    global answer
    answer = 0
    
    if sum(a) != 0:
        return -1
    
    edge = [[] for _ in range(len(a))]
    visit = [0 for _ in range(len(a))]
    for u, v in edges:
        edge[u].append(v)
        edge[v].append(u)
    
    dfs(0)
    
    return answer

# 0번 노드를 루트노드로 놓고 dfs를 돌린다.
# 마지막 노드까지오면 그 노드 값을 리턴한다
# 그러면 부모노드에 그 리턴값을 더해주고, answer값에는 절댓값으로 더해준다.