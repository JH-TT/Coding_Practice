import sys

input = sys.stdin.readline

s = input().rstrip()
n = len(s)

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
res = [float('inf')] * (n + 1)
res[0] = 0

# 한 개는 펠린드롬
for i in range(1, n + 1):
    dp[i][i] = 1

# 2개가 서로 같으면 펠린드롬
for i in range(1, n):
    if s[i - 1] == s[i]:
        dp[i][i + 1] = 1

# 양쪽 문자가 같고, 그 내부 문자열이 펠린드롬이면 양쪽 문자 합쳐도 펠린드롬이 유지됨.
for i in range(2, n):
    for j in range(1, n + 1 - i):
        if s[j - 1] == s[j + i - 1] and dp[j + 1][i + j - 1] == 1:
            dp[j][i + j] = 1

# 이 부분에 대한 내용은 https://yabmoons.tistory.com/592 여기 마지막 부분 참고.
for end in range(1, n + 1):
    for start in range(i + 1):
        if dp[start][end] != 0:
            res[end] = min(res[end], res[start - 1] + 1)
print(res[n])

# 전체적인 내용은 https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80 참고