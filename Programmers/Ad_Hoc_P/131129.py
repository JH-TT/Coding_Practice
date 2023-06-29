def solution(target):
    dp = [[0, 0] for _ in range(target+61)]
    dp[50] = [1, 1] # 던진횟수, 싱글 혹은 불을 맞춘 횟수
    points = [50]
    for i in range(1, 21):
        dp[i] = [1, 1]
        dp[i*2] = [1, 0]
        dp[i*3] = [1, 0]
        points.append(i)
        points.append(i*2)
        points.append(i*3)
    points = sorted(list(set(points)))
    
    for i in range(1, target):
        if dp[i][0] == 0:
            continue
        for p in points:
            flag = 0
            if p == 50 or 1 <= p <= 20:
                flag = 1
            if dp[i+p][0] == 0:
                dp[i+p] = [dp[i][0]+1, dp[i][1]+flag]
            elif dp[i][0]+1 < dp[i+p][0]:
                dp[i+p] = [dp[i][0]+1, dp[i][1]+flag]
            elif dp[i][0]+1 == dp[i+p][0]:
                dp[i+p][1] = max(dp[i+p][1], dp[i][1]+flag)
    return dp[target]

# dp를 이용한 문제
# 총 포인트의 개수는 42개이고 이 중에서 잘 뽑아 총합 target을 딱 맞추면 된다.
# 풀이 순서
# 1. 현재 점수 + 각 가능한 포인트들을 해서 현재점수+p의 정보와 비교해서 교체한다.
# 2. 이중 for문으로 처리한다.

# N이 248이후로는 N+60과 다트 1발 차이라고 한다.
# 수정한 풀이 평균 5ms로 풀이가능
def solution(target):
    dp = [[0, 0] for _ in range(311)]
    dp[50] = [1, 1] # 던진횟수, 싱글 혹은 불을 맞춘 횟수
    points = [50]
    for i in range(1, 21):
        dp[i] = [1, 1]
        dp[i*2] = [1, 0]
        dp[i*3] = [1, 0]
        points.append(i)
        points.append(i*2)
        points.append(i*3)
    points = sorted(list(set(points)))
    
    for i in range(1, 251):
        if dp[i][0] == 0:
            continue
        for p in points:
            flag = 0
            if p == 50 or 1 <= p <= 20:
                flag = 1
            if dp[i+p][0] == 0:
                dp[i+p] = [dp[i][0]+1, dp[i][1]+flag]
            elif dp[i][0]+1 < dp[i+p][0]:
                dp[i+p] = [dp[i][0]+1, dp[i][1]+flag]
            elif dp[i][0]+1 == dp[i+p][0]:
                dp[i+p][1] = max(dp[i+p][1], dp[i][1]+flag)
                
    cnt, cnt2 = 0, 0
    if target > 310:
        target -= 250
        cnt = target // 60
        cnt2 = target % 60
        cnt2 += 250
        dp[cnt2][0] += cnt
        target = cnt2
    
    return dp[target]

# 대략 250쯤 부터는 무조건 60이 들어가기 때문에 dp를 310정도까지만 구하고 
# target이 310이 넘어가면 60씩 빼서 250과 310 사이에 오면 다트 수를 60을 뺀 횟수를 더하고 리턴한다.