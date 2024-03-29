import heapq


# 캐시를 이용해서 팩토리얼을 미리 구해놓는다.
global cache
cache = [0] * 21
cache[0], cache[1] = 1, 1
for i in range(2, 21):
    cache[i] = i * cache[i-1]
    
def factorial(n):
    global cache
    return cache[n]

def solution(n, k):
    answer = []
    q = []
    for i in range(1, n+1):
        heapq.heappush(q, i)

    cnt = 1
    while q:
        all_case = factorial(n - cnt)
        d = k // all_case
        r = k % all_case
        # 나머지가 0이면 d에서 하나 뺀다.
        if r == 0:
            d -= 1
            r += all_case
        arr = []
        for _ in range(d):
            heapq.heappush(arr, heapq.heappop(q))
        answer.append(heapq.heappop(q))
        while arr:
            heapq.heappush(q, heapq.heappop(arr))
        k = r
        cnt += 1

    return answer

# 다른 사람 코드
from math import factorial
def solution(n, k):
    answer = []
    nums = list(range(1, n+1))
    order = []
    k -= 1
    for i in range(n-1, -1, -1):
        temp = factorial(i)
        q, r = divmod(k, temp)
        k = r
        order.append(q)
    # print(order) 2 0 0 이런식으로 나오면 2번쨰 0번째 0번째 숫자를 pop한다고 보면 됨.
    for idx in order:
        answer.append(nums.pop(idx))

    return answer