from collections import deque, defaultdict

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    global cnt
    q = deque()
    visit[a][b] = 1
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue

            if visit[nx][ny]:
                continue
            # 방문처리
            visit[nx][ny] = 1
          
            # 현재 위치가 열쇠거나 문이면
            if arr[nx][ny].isalpha():
                # 문일경우 -> 열쇠가 있으면 지나가고, 없으면 위치만 저장해 놓는다.
                if arr[nx][ny].isupper():
                    if arr[nx][ny].lower() not in key:
                        door[arr[nx][ny]].append([nx, ny])
                    else:
                        q.append([nx, ny])
                # 열쇠일 경우 -> 중복되는 열쇠면 넘기고 새로운 열쇠면 현재 열쇠와 맞는 문의 위치를 q에 넣는다.(위치가 저장된 문만)
                else:
                    if arr[nx][ny] not in key:
                        key.add(arr[nx][ny])
                        # 현재 열쇠로 열 수 있는 문의 위치들을 전부 q에 넣음
                        for cor in door[arr[nx][ny].upper()]:
                            q.append(cor)
                    q.append([nx, ny])                  
            elif arr[nx][ny] != "*":
                # 찾고자 하는 문서면 cnt증가
                if arr[nx][ny] == "$":
                    print(nx, ny)
                    cnt += 1
                q.append([nx, ny])
                

for test in range(int(input())):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    visit = [[0 for _ in range(w)] for _ in range(h)] # 방문처리
    door = defaultdict(list) # 문의 위치 정보
    a = set(input()) # 열쇠정보
    cnt = 0
    if a == "0":
        key = set()
    else:
        key = a
    
    for i in range(h):
        for j in range(w):
            if 0 < i < h-1 and 0 < j < w-1:
                continue
            if arr[i][j] != "*" and not visit[i][j]:
                if arr[i][j] == ".":
                    bfs(i, j)
                elif arr[i][j] == "$":
                    cnt += 1
                    bfs(i, j)
                elif arr[i][j].isalpha():
                    if arr[i][j].isupper():
                        if arr[i][j].lower() not in key:
                            door[arr[i][j]].append([i, j])
                        else:
                            bfs(i, j)
                    else:
                        if arr[i][j] not in key:
                            key.add(arr[i][j])
                            for cor in door[arr[i][j]]:
                                bfs(cor[0], cor[1])

    print(f"case : {test} -> cnt : {cnt}")

# 일반 bfs보다는 꽤나 신경쓸게 있던 문제
# 조건문의 개수도 많고, 열쇠를 주웠을때 이미 지난 문들을 처리해야한다는 것. 이 두 개가 꽤나 코드를 길게 만들었음.