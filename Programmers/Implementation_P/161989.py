def solution(n, m, section):
    answer = 0
    start = section[0]
    for s in section[1:]:
        if s - start >= m:
            answer += 1
            start = s
    
    return answer + 1


# 첨에는 그냥 첫 색칠할 부분부터 마지막 부분까지 길이를 구해서 몫, 나머지를 이용한 풀이로 했지만
# 만약에 [2, 3, 15, 16]이고 페인트 길이는 4라고 가정하면
# 첨에 푼 방식을 이용하면 전부 색칠된 부분을 한 번 더 덧칠하는 부분이 생기니 최소색칠횟수가 되지 않는다.
# 따라서 하나씩 확인하면서 페인츠칠 1번했으면 다음 색칠할 부분까지는 스킵해야 하는 점을 이용한다.