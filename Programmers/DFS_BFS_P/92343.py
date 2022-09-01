def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []
    def dfs(sheep, wolf):
        if sheep > wolf: # 양이 늑대보다 많을때 마다 넣어준다.
            answer.append(sheep)
        else: # 늑대가 많으면 이후 탐색 종료
            return
        for i in range(len(edges)):
            parent = edges[i][0]
            child = edges[i][1]
            iswolf = info[child]
            # edge 하나씩 전부 보면서 부모노드를 방문했고 자식노드는 방문안했으면 진행
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep+(iswolf==0), wolf+(iswolf==1))
                visited[child] = 0
    dfs(1, 0)
    return max(answer)