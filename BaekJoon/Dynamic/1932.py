n = int(input())

num = []
for _ in range(n):
    # 입력받는 숫자들 양쪽에 0을 넣어서 인덱스가 입력받지 않은 숫자를 가리키면 0을 더하도록 한다.
    b = [0]
    b += list(map(int, input().split()))
    b += [0]
    num.append(b)

for i in range(1, n):
    for j in range(1, len(num[i]) - 1):
        num[i][j] = num[i][j] + max(num[i - 1][j - 1], num[i - 1][j]) # 왼쪽 대각선이랑 오른쪽 대각선 중에 더 큰 값을 더한다.
print(max(num[n - 1]))