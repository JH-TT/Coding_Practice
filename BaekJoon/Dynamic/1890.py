import sys
input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
visit[0][0] = 1

for i in range(n):
    for j in range(n):
        # 끝에 다다르면 출력 후 종료.
        if i == n - 1 and j == n - 1:          
            print(visit[i][j])
            exit(0)
        # 아니면 범위를 벗어나지 않는 한에서 현재자리 지나간 횟수를 다음에 넘어갈 곳에 더해준다.
        if visit[i][j] > 0:
            if i + arr[i][j] < n:
                visit[i + arr[i][j]][j] += visit[i][j]
            if j + arr[i][j] < n:
                visit[i][j + arr[i][j]] += visit[i][j]