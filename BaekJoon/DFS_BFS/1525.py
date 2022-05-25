from collections import deque, defaultdict

def bfs():
    q = deque()
    q.append(p)

    while q:
        p_2 = q.popleft()

        if p_2 == "123456780": # 배열완성되면 움직인 횟수를 리턴
            return visited[p_2]
        idx = p_2.index('0') # 빈 공간 위치 찾기

        # 퍼즐을 2차원 리스트로 만들경우의 인덱스값들
        x = idx // 3
        y = idx % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > 2 or ny < 0 or ny > 2:
                continue
            
            t = nx * 3 + ny # 문자열로 나타냈을떄 인덱스
            ts = list(p_2) # 문자열을 리스트로 변경
            ts[idx], ts[t] = ts[t], ts[idx] # 빈곳을 이동시킴.
            ti = "".join(ts) # 다시 문자열로 변경
            if not visited[ti]: # 첫 배열이면 deque에 넣는다.
                visited[ti] = visited[p_2] + 1
                q.append(ti)
    return -1
        
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = defaultdict(int) # 배열을 만드는데 움직이는 횟수.
p = '' # 퍼즐을 문자열로 저장
for _ in range(3):
    a = "".join(map(str, input().split()))
    p += a
  
print(bfs())

# 메모리가 적어서 문자열로 해결함.