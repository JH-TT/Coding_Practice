from collections import deque

# 오른쪽, 아래만 이동가능
dx = [0, 1]
dy = [1, 0]

n = int(input())
min_v = 10**6 # 최솟값
max_v = -10**6 # 최댓값

graph = [input().split() for _ in range(n)]
q = deque()
q.append((0, 0, graph[0][0]))
while q:
    x, y, e = q.popleft()
    # 끝까지 갔으면 최대와 최소를 구한다.
    if x == n-1 and y == n-1:
        min_v = min(min_v, int(e))
        max_v = max(max_v, int(e))
        continue
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # e가 만약 식이 맞게 구성돼 있으면 try부분대로 갈것이고
        # eval함수는 Integer로 리턴해 준다. 따라서 e + graph[nx][ny]가 오류가 걸린다는 것은 e가 Integer형태기 때문에 문자열과 결합이 안돼 예외가 발생한다.
        # e가 Integer 형태라는 것은 식이 만들어져 계산되었다는 의미이므로 operator가 와야한다. 따라서 except로 진행하게 된다.(파이썬은 정수와 문자열은 더할 수 없다.)
        # isdigit 함수는 음수, 소수점을 문자로 판단해 "-10"같은건 False가 출력된다고 함.
        try:
            q.append((nx, ny, eval(e + graph[nx][ny])))
        except:
            q.append((nx, ny, str(e) + graph[nx][ny]))
print(max_v, min_v)

# bfs로 전부 확인해서 최소와 최대를 구한다.