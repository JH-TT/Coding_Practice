import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (m + 1)]

# 리스트 인덱스 오류를 없애기 위해 위쪽과 왼쪽 테두리에 0으로 채운다.
for _ in range(n):
    a = [0] + list(map(int, input().rstrip()))
    arr.append(a)
max_square = 0

# 왼쪽, 11시 대각선, 위쪽 중 최솟값을 더한다.
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 현재 값이 0인 부분은 건너뛴다.
        if arr[i][j] == 0:
            continue
        arr[i][j] += min(arr[i-1][j], arr[i][j-1], arr[i-1][j-1])
    max_square = max(max_square, max(arr[i])) # 최댓값 계속 갱신
print(max_square ** 2)