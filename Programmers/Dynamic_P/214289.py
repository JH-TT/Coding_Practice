def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    N = len(onboard)
    # 최소가 -10이기에 배열을 이용하려면 10 더해준다.
    temperature += 10
    t1 += 10
    t2 += 10
    INF = 10**9
    
    # 가로는 시간, 세로는 온도, 값은 소비전력
    dp = [[INF for _ in range(52)] for _ in range(N)]
    dp[0][temperature] = 0

    for i in range(1, N):
        start = 0
        end = 0
        # 효율적으로 처리하기 위해 범위를 미리 정한다.
        # 아무리 온도가 왔다갔다해도 t1, t2, temperature를 넘어서는 경우는 없을것이다.
        if onboard[i]:
            start = t1
            end = t2
        else:
            start = min(t1, temperature)
            end = max(t2, temperature)
        for j in range(start, end+1):
            # j온도가 temperature보다 적으면
            # i-1분에 j+1온도는 j온도로 temperature반대 방향으로 변하니 a비용이 든다.
            # i-1분 j온도를 유지하려면 b비용이 든다. (외부온도와 같지 않아서 온도를 유지하려면 에어컨을 사용할 수 밖에 없다.)
            if j < temperature:
                # 0인경우에 인덱스범위때매 조건을 넣음
                if j == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j+1] + a, dp[i-1][j] + b)
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1], dp[i-1][j+1] + a, dp[i-1][j] + b)
            # 위 방식과 같음
            elif j > temperature:
                dp[i][j] = min(dp[i][j], dp[i-1][j-1] + a, dp[i-1][j+1], dp[i-1][j] + b)
            # 외부온도와 같으면 에어컨을 사용하지 않아서 해당 온도로 변하기 때문에 비용이 들지 않는다.
            else:
                if j == 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i-1][j+1])
                else:
                    dp[i][j] = min(dp[i][j], dp[i-1][j], dp[i-1][j+1], dp[i-1][j-1])
    
    return min(dp[N-1])

# 링크참고 : https://school.programmers.co.kr/questions/52432
# 저 링크를 봐도 추가적으로 생각할 부분이 있었다.