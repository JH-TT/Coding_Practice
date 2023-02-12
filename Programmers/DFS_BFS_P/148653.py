from collections import deque

def solution(storey):
    answer = 10**10
    q = deque()
    q.append((storey, 0, 0))
    while q:
        s, pos, cnt = q.popleft()
        k = int(list(str(s))[::-1][pos])
        # 이미 최솟값을 넘겼거나 다 확인했으면 더이상 볼 필요가 없다.
        if cnt >= answer:
            continue
        # 마지막 자릿수면 5를 기준으로 확인한다.
        if pos == len(str(s)) - 1:
            if int(list(str(s))[-1]) <= 5:
                answer = min(answer, cnt + int(list(str(s))[0]))
            else:
                answer = min(answer, cnt + (10 - int(list(str(s))[0])) + 1)
            continue
        # 5 미만이면 빼고, 5 초과면 더한다. 5면 뺀거 더한거 둘 다 넣는다.
        if list(str(s))[::-1][pos] < '5':
            q.append((s - k * (10 ** pos), pos+1, cnt+k))
        elif list(str(s))[::-1][pos] > '5':
            q.append((s + (10 - k) * (10 ** pos), pos+1, cnt+(10-k)))
        else:
            q.append((s - 5 * (10 ** pos), pos+1, cnt+5))
            q.append((s + 5 * (10 ** pos), pos+1, cnt+5))
    
    return answer


# 짧은 코드
def solution(storey):
    if storey < 10 :
        return min(storey, 11 - storey) # 마찬가지로 한번에 뺄지 더하고 뺄지 확인하는 코드
    left = storey % 10
    return min(left + solution(storey // 10), 10 - left + solution(storey // 10 + 1)) # 더한경우, 뺀 경우

# 나도 dfs를 생각했지만 이렇게 간단하게 구현하는 방식은 생각하지 못함.