from collections import deque

def bfs(arr, target):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visit = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]

    q = deque()
    q.append((0, 0))
    visit[0][0] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= len(arr) or ny < 0 or ny >= len(arr[0]):
                continue

            if visit[nx][ny]:
                continue

            visit[nx][ny] = 1
            if arr[nx][ny] == '-':
                q.append((nx, ny))

            if arr[nx][ny] == target:
                arr[nx][ny] = '-'

    return arr

def crane(arr, target):
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0]) - 1):
            if arr[i][j] == target:
                arr[i][j] = '-'

    return arr

def solution(storage, requests):
    answer = 0
    arr = [['-' for _ in range(len(storage[0]) + 2)]]

    for s in storage:
        arr.append(['-'] + list(s) + ['-'])
    arr.append(['-' for _ in range(len(storage[0]) + 2)])

    for r in requests:
        target = r[0]
        if len(r) == 2:
            arr = crane(arr, target)
        else:
            arr = bfs(arr, target)

    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[0])-1):
            if arr[i][j] != '-':
                answer += 1

    return answer

# 그냥 완탐문제
# 다만 겉에만 탐색할땐 BFS를 이용했음.