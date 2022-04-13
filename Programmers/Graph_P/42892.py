import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    def dfs(v):
        if v == 0:
            return
        preorder.append(v) # 전위순회는 먼저 확인하니까 재귀전에 넣음
        dfs(ryan[v][0])
        dfs(ryan[v][1])
        postorder.append(v) # 후위순회는 다 확인 후 끝에서 확인하는거니까 재귀끝나고 넣음
    
    answer = []
    preorder = [] # 전위순회 리스트
    postorder = [] # 후위순회 리스트
    
    sortnode = sorted(nodeinfo, key=lambda x : (-x[1], x[0])) # x 값을 기준으로 내림차순정렬
    ryan = [[0, 0] for _ in range(len(nodeinfo) + 1)] # 각 노드들의 자식노드 정보
    first = nodeinfo.index(sortnode[0]) + 1 # 젤 위의 노드
    
    for n in sortnode[1:]: # 다음 노드부터 돌면서 확인
        key = nodeinfo.index(n)
        node = first
        while 1:
            if n[0] < nodeinfo[node-1][0]: # 현재노드의 x값이 더 작으면 왼쪽 노드탐색
                if ryan[node][0] == 0: # 더이상 자식노드가 없으면 넣음
                    ryan[node][0] = key+1
                    break
                node = ryan[node][0]
            else:                          # 현재노드의 x값이 더 크면 오른쪽 노드탐색
                if ryan[node][1] == 0:
                    ryan[node][1] = key + 1
                    break
                node = ryan[node][1]
                
    dfs(first) # 탐색시작
    answer.append(preorder)
    answer.append(postorder)
    
    return answer

# 이 문제는 처음에 클래스를 작성해서 하려다가 아직 클래스 부분은 미숙해서 포기.
# 재귀 깊이가 얕아서 setrecursionlimit을 이용