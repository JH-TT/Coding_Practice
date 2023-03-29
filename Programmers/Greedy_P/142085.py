# 첫 풀이
import heapq

def solution(n, k, enemy):
    answer = 0
    num = []

    if k == len(enemy):
        return k

    for e in enemy:
        # n이 여유가 있으면 넣는다.
        if n >= e:
            heapq.heappush(num, -e)
            n -= e
            answer += 1
            continue
        # 만약 n이 부족하면 k를 사용한다.
        # k가 없으면 바로 종료.
        if k == 0:
            break
        # k가 있으면 방어하고 k를 1줄인다.
        if num and e <= -num[0]:
            n += -heapq.heappop(num)-e
            heapq.heappush(num, -e)
        k -= 1
        answer += 1

    return answer

# 좀 더 최적화된 코드
# 미리 enemy에서 k번째 인덱스까지 넣어둔다. 그 후에 heap으로 변경
# 그 뒤로 들어오면 그 숫자를 넣고 그중에 최솟값을 꺼내서 n을 뺀다.
# n이 음수면 그대로 종료. 그 외에는 인덱스값이 답이된다.
import heapq

def solution(n, k, enemy):
    answer = 0
    num = enemy[:k]
    heapq.heapify(num)
    if k == len(enemy):
        return k
    
    for i in range(k, len(enemy)):
        n -= heapq.heappushpop(num, enemy[i])
        if n < 0:
            return i
        
    return len(enemy)

# heappushpop을 새로 알게됨....