n = int(input())
arr = list(map(int, input().split()))

d = [0] * (1_000_000 + 1) # 배열이 존재하는지 check하는 딕셔너리
dp = [0] * (1_000_000 + 1) # 각 숫자마다 점수
m = 0 # 주어진 수 중에 최댓값
for a in arr:
    d[a] = 1
    m = max(m, a)

# 가장 큰 수는 무조건 점수를 획득할 수 없기 때문에 해당 수의 약수중에 자신을 제외한 가장 큰 수까지만 확인한다.
for i in range(1, int(m * 1/2) + 1):
    # 당연히 주어진 숫자가 아니면 스킵한다.
    if d[i] == 0:
        continue
    # 자기 자신은 제외
    j = 2
    while j * i <= m:
        # 당연히 배수가 주어진 수에 없으면 스킵
        if d[i * j] == 0:
            j += 1
            continue
        # 주어진 리스트에 존재한다면 그 수(i * j)는 현재 숫자(i)의 배수이기 때문에 감점이되고, 현재 숫자는 득점을 한다.
        dp[i * j] -= 1
        dp[i] += 1
        j += 1

for a in arr:
    print(dp[a], end= ' ')