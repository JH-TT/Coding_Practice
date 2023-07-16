# 1번째 방식 (이분탐색 + 구현)
# 돌의 숫자를 기준으로 이분탐색으로 비교해서 찾아본다.
# 효율성 3개 시간초과

# 2번째 방식 (슬라이싱 윈도우 이용)
# k개가 연속으로 0이면 되니까 k크기의 윈도우를 옮기면서 비교한다.
# 효율성 13번 시간초과

# 3번째 방식 (슬라이싱 윈도우 좀 더 효율적으로)
# 최댓값 갱신을 최대한 빠르게 찾을 수 있도록
from collections import deque

def solution(stones, k):
    q = deque()
    answer = float('inf')
    for i, v in enumerate(stones):
        if q and q[0]+k <= i:
            q.popleft()
        while q and stones[q[-1]] <= v:
            q.pop()
        q.append(i)
        if i < k-1:
            continue
        answer = min(answer, stones[q[0]])

    return answer

# 이분탐색인줄 알았지만.... 효율성에서 바로 시간초과..
# 슬라이싱 윈도우가 답이었다. O(N)에 가깝게 푸는게 정답