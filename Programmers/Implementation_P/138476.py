from collections import Counter

def solution(k, tangerine):
    answer = 0
    t = sorted(list(Counter(tangerine).values()), reverse=True)
    total = 0
    for i in t:
        total += i
        answer += 1
        if total >= k:
            break
    return answer

# 그냥 적은 종류의 개수로 k개를 뽑는 문제이다.
# 개수를 기준으로 내림차순으로 정렬한 뒤, k개가 넘을때까지 종류의 수를 더한다.