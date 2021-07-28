n, k = map(int, input().split())

ans = [[0 for _ in range(k + 1)] for _ in range(n)]

for i in range(n):
    w, v = map(int, input().split())

    for j in range(1, k + 1):
        if j >= w:
            ans[i][j] = max(ans[i - 1][j], ans[i - 1][j - w] + v)
        else:
            ans[i][j] = ans[i - 1][j]
print(max(ans[-1]))
# knapsack problem으로 유명한 문제라함.
# https://huiyu.tistory.com/entry/DP-01-Knapsack%EB%B0%B0%EB%82%AD-%EB%AC%B8%EC%A0%9C 왜 코드가 저렇게 짜여졌는지 상세하게 나옴.