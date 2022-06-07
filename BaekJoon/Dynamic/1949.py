import sys
sys.setrecursionlimit(10**6)

def dfs(cur):
    visit[cur] = 1
    for u in edge[cur]:
        if not visit[u]:
            dfs(u)
            # cur이 현재 우수 마을이면 당연히 다음 마을은 우수 마을이 될 수 없음
            dp[cur][1] += dp[u][0]
            # cur이 우수마을이 아니면 다음 마을은 우수 마을이 될 수도, 안 될 수도 있음(둘 중에 더 많은 경우)
            dp[cur][0] += max(dp[u][1], dp[u][0])

n = int(input())
people = [0] + list(map(int, input().split()))
dp = [[0, people[i]] * 2 for i in range(n+1)]
edge = [[] for _ in range(n+1)]
visit = [0 for _ in range(n + 1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

dfs(1)
print(max(dp[1][1], dp[1][0]))

# dp[i][0] : i 마을을 우수 마을로 선정하지 않았을 경우
# dp[i][1] : i 마을을 우수 마을로 선정한 경우
# 루트노드를 1 기준으로 놓고 dfs를 돌려서 해결
# 참고 : https://cotak.tistory.com/29