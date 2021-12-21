from bisect import bisect_left

def solution(citations):
    answer = 0
    citations.sort()
    for i in range(citations[-1]):
        if len(citations) - bisect_left(citations, i) >= i: # 현재 인용된 횟수가 지금 횟수 이상인 것의 개수보다 작거나 같을때마다 업데이트
            answer = i


    return answer

# 다른 풀이 1
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1))) # 인덱스는 1번부터 해서, citations에서 (index, value)중에 작은값들만 저장하고 마지막에 그 값들중 최댓값을 answer로 지정한다.
    return answer

# 다른 풀이 2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0