def dfs(N, before):
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        after[i][N:N+2*N-1] = before[i]
      
    k = 0
    for i in range(N, 2*N):
        print(before[k])
        print(len(before[k]))
        after[i][:2*N] = before[k]
        after[i][2*N:2*N+len(before[k])] = before[k]
        k += 1

    if 2 * N == n:
        return after

    return dfs(2*N, after)
    

n = int(input())

pattern = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]

if n == 3:
    res = pattern
else:
    res = dfs(3, pattern)

for i in res:
    print("".join(i))


# 이전 모양을 그대로 붙여넣는 느낌으로 풀어냈음.
# 즉 아예 범위에 맞게 2차원 리스트로 만들고 각 자리에 하나씩 넣는 느낌으로