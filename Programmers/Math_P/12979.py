def solution(n, stations, w):
    answer = 0
    left = 0
    for stat in stations:
        right = stat - w
        if left >= right:
            left = stat + w
            continue
        answer += ((right - left - 1 + 2*w) // (2*w + 1))
        left = stat + w
    
    if left < n+1:
        answer += ((n - left + 2*w) // (2*w + 1))

    return answer

# 비둘기집 원리를 이용하는 문제