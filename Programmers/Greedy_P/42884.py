def solution(routes):
    answer = 1
    routes = sorted(routes, key = lambda x : x[1])
    
    m = routes[0][1]
    for i in range(1, len(routes)):
        if routes[i][0] > m:
            m = routes[i][1]
            answer += 1
    
    
    return answer

# 풀이접근
# 나오는 지점도 포함이므로, 각 차들이 나오는 지점을 오름차순으로 정렬하고
# 처음 나오는 지점을 시작으로 다른 차들의 시작지점이 그 처음 나오는 지점보다 앞이면
# 나오는 지점을 새로 업데이트한다. 이런식으로 n개의 차들을 탐색.