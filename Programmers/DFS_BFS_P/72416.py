import sys
sys.setrecursionlimit(10**7)

def solution(sales, links):

    def dfs(now):
        min_cost = 0
        min_diff = 0
        flag = False

        for child in graph[now]:
            dfs(child)

            minValue = min(dp[child][0], dp[child][1])
            # 팀원이 참여한 경우가 최소가 되면
            # 상사는 참여를 하든 안하든 상관없게 된다.
            if minValue == dp[child][1]:
                flag = True
            min_cost += minValue
            diff = dp[child][1] - dp[child][0]
            if diff > 0:
                if min_diff == 0:
                    min_diff = diff
                else:
                    min_diff = min(min_diff, diff)
        # 상사가 참여하는 경우는 본인 + 부하직원의 최솟값들의 합을 더하면 된다.        
        dp[now][1] = sales[now] + min_cost
        # 상사가 참여하지 않는 경우 (2가지 경우)
        # 1. 부하직원 중에 한 명이라도 본인이 참여한 경우가 최소가 되는 경우
        if flag:
            dp[now][0] = min_cost
        # 2. 부하직원 중에 아무도 참여하지 않으면 참여할 경우 비용차이가 가장 작은 값을 더해준다.
        else:
            dp[now][0] = min_cost + min_diff

    answer = 0
    sales = [0] + sales    
    graph = [[] for _ in range(len(sales))]
    dp =[[0, 0] for _ in range(len(sales))]

    for a, b in links:
        graph[a].append(b)

    dfs(1)

    return min(dp[1][0], dp[1][1])

# 문제 풀이는 https://school.programmers.co.kr/questions/34874 참조