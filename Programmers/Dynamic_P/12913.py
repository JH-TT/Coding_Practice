def solution(land):
    answer = 0
    for i in range(1, len(land)):
        for j in range(4):
            max_num = 0
            for k in range(4):
                if j == k: continue
                max_num = max(max_num, land[i-1][k])
            land[i][j] += max_num
    return max(land[-1])

# 이전 행에서 현재 행을 제외한 나머지중에 최댓값을 더해나간다.
# 그러면 마지막 행에는 각각 값들이 있고 그 중에 최댓값을 리턴하면 된다. 