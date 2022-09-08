from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    tot1 = sum(q1)
    tot2 = sum(q2)
    answer = -1
    if sum(q1) == sum(q2):
        return 0
    if sum(q1 + q2) % 2 == 1:
        return -1
    
    cnt1 = 0
    cnt2 = 0
    
    while 1:
        # 서로 한바퀴 돌았는데도 못찾으면 그대로 종료
        if cnt1 >= len(q1) and cnt2 >= len(q2):
            break

        # 두 리스트 원소 합이 같으면 종료
        if tot1 == tot2:
            answer = cnt1 + cnt2
            break

        # 1번 큐가 더 많으면 2번에 넘김
        if tot1 > tot2:
            num = q1.popleft()
            q2.append(num)
            tot1 -= num
            tot2 += num
            cnt1 += 1
        # 반대
        else:
            num = q2.popleft()
            tot2 -= num
            tot1 += num
            q1.append(num)
            cnt2 += 1
    
    return answer

# 리스트 하나로 푼 정답
def solution(que1, que2):
    queSum = (sum(que1) + sum(que2)) # 전체 합
    if queSum % 2: # 홀수면 절대 못찾으니 바로 -1 리턴
        return -1
    target = queSum // 2 # 절반으로 나눔.

    n = len(que1)
    start = 0 # start는 1번큐 첫번째 원소 start 이전은 2번큐 원소로 생각
    end = n - 1 # end가 어떻게 보면 2번리스트에서 1번에 넣은거로 생각
    ans = 0

    cur = sum(que1)
    que3 = que1 + que2 # 리스트를 합친다.
    while cur != target:
        if cur < target:
            end += 1
            if end == n * 2:
                return -1
            cur += que3[end]
        else:
            cur -= que3[start]
            start += 1
        ans += 1
    return ans

# 이 풀이는 투포인터 느낌으로 풀었다. 보기엔 좀 더 깔끔해 보임