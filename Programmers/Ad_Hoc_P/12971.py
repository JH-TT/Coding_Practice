def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)
    # 0번 인덱스를 빼는 경우
    dp1 = [s for s in sticker[:-1]]
    for i in range(1, len(dp1)):
        if i == 1:
            dp1[i] = max(dp1[i], dp1[i-1])
        else:
            dp1[i] = max(dp1[i-1], dp1[i-2] + dp1[i])
    # 1번 인덱스를 빼는 경우
    dp2 = [s for s in sticker[1:]]
    for i in range(1, len(dp1)):
        if i == 1:
            dp2[i] = max(dp2[i], dp2[i-1])
        else:
            dp2[i] = max(dp2[i-1], dp2[i-2] + dp2[i])

    return max(dp1[-1], dp2[-1])

# 1번 스티커를 먼저 빼는 경우와
# 2번 스티커를 먼저 빼는 경우 2가지를 따져서 그 중에 최댓값을 구하는 문제였다.
# 왜 1, 2번만 뺴냐. 양쪽에 1개씩만 사용하지 못하기 때문에 아무리 많이 떨어져서 뜯어봐야 2칸이다. 그래서 1, 2번을 기준으로 나눈것이다.
