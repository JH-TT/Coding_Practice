def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    for i in range(m-1, len(score), m):
        answer += score[i] * m
    
    return answer

# 핵심 : m개의 사과를 담아서 그 중에 최솟값을 기준으로 점수를 구하니까 정렬을 해서 처리하면 된다.
# 내림차순으로 정렬을 하게되면 m개를 순서대로 담았을 때 마지막 사과가 최저 점수이니 그 부분을 생각해서 for loop를 돌 때 m개씩 뛰어넘어서 확인만 하면 된다.