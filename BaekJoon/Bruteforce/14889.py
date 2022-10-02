import sys
input = sys.stdin.readline

def dfs(team, cnt):
    global res
    # 팀이 결성되면 점수 계산
    if cnt == n // 2:
        t1 = 0
        t2 = 0
        team2 = []
        for i in range(n):
            if i in team:
                continue
            team2.append(i)
        for i in range(n//2):
            for j in range(i+1, n//2):
                t1 += graph[team[i]][team[j]]
                t1 += graph[team[j]][team[i]]
                t2 += graph[team2[i]][team2[j]]
                t2 += graph[team2[j]][team2[i]]
        res = min(res, abs(t1 - t2))
        return
    for i in range(team[-1]+1, n):
        dfs(team + [i], cnt+1)
            

n = int(input())
graph = []
total = 0
for _ in range(n):
    score = list(map(int, input().split()))
    total += sum(score)
    graph.append(score)
global res
res = float('inf')

for i in range(n//2+1):
    dfs([i], 1)
print(res)

# 그냥 조합문제. 난 itertools를 안쓰고 풀어본것.