import sys
input = sys.stdin.readline

N = int(input())
pal = list(map(int, input().split()))
M = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)] # i부터 j까지 수열이 팰린드롬인지 아닌

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for start in range(N-i):
        end = start + i
        
        if start == end:
            dp[start][end] = 1
        elif pal[start] == pal[end]:
            if abs(start-end) == 1:
                dp[start][end] = 1
            elif dp[start+1][end-1]:
                dp[start][end] = 1

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])

# 이 문제는 dp를 어떻게 돌릴지가 관건
# 괜히 start+1 ~ end-1이 팰린드롬이면 start, end가 같은 숫자면 start~end가 팰린드롬인걸 알고
# 그냥 이중for문을 작성하면 start+1 ~ end-1 부분이 초기화가 안돼있어 틀리게 된다.
# 그래서 start를 먼저 움직여서 확인하도록 구현하는것이 관건이었다.
# 그걸 생각해서 하는것이 이중 for문을 start와 end로 돌리는것이 아닌,
# 부분수열의 길이, start로 돌리고 end는 start + 부분수열의 길이로 풀어나가야 start+1 ~ end-1이 초기화되어 해결할 수 있게 된다.