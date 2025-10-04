# [x, y, z]
# x : 일자형으로 만나는 경우
# y : 대각선으로 만나는 경우
# z : 수직으로 만나는 경우

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dynamic = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
dynamic[0][1] = [1, 0, 0]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        # 오른쪽으로 이동하는 경우
        # 오른쪽으로 이동하려면 현재 위치에 일자형 또는 대각선인 경우에 이동이 가능하다
        if j < n - 1:
            if arr[i][j + 1] == 0:
                dynamic[i][j + 1][0] += (dynamic[i][j][0] + dynamic[i][j][1])
              
        # 대각선으로 이동하는 경우
        # 대각선으로 이동하려면 모든 경우에 대해 이동이 가능하다.
        if i < n - 1 and j < n - 1:
            if arr[i + 1][j] == 0 and arr[i + 1][j + 1] == 0 and arr[i][j + 1] == 0:
                dynamic[i + 1][j + 1][1] += sum(dynamic[i][j])
              
        # 아래로 이동하는 경우
        # 아래의 경우에는 대각선, 수직의 경우에만 이동이 가능하다
        if i < n - 1:
            if arr[i + 1][j] == 0:
                dynamic[i + 1][j][2] += (dynamic[i][j][1] + dynamic[i][j][2])

print(sum(dynamic[-1][-1]))