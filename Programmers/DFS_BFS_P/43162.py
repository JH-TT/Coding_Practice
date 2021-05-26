from collections import deque

def solution(n, computers):
    answer = 0 # 결과값
    visit = [0] * n
    for i in range(n):
        if visit[i]: # 방문했으면 넘김.
            continue
        q = deque([i]) # q에 i를 넣는다.
        visit[i] = 1 # 방문표시.
        while q:
            x = q.popleft()
            for j in range(n):
                if not visit[j] and computers[x][j]: # j컴퓨터에 방문하지 않았고, x컴퓨터와 연결돼 있다면 방문처리하고 q에 넣음.
                    visit[j] = 1
                    q.append(j)
        answer += 1 # while문을 다 돌면 한 그룹이 끝난거니 answer에 1을 추가함.
    
    return answer