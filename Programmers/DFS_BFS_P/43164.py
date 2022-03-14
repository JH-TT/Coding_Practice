# 재귀이용
from collections import defaultdict, deque

def solution(tickets):
    answer = []
    route = defaultdict(list)
    for a, b in tickets:
        route[a].append(b)        
    
    q = deque()
    rest_tickets = list(tickets)
    q.append((["ICN"], rest_tickets))
    
    while q:
        r, t = q.popleft()
        dest = r[-1]
        if len(r) == len(tickets) + 1:
            answer.append(r)
            
        if not route[dest]:
            continue
          
        # 현 시점에서 갈 수 있는 모든 경우를 본다.
        for d in route[dest]:
            if [dest, d] not in t:
                continue

            t.remove([dest, d])
            q.append((r + [d], list(t)))
            t.append([dest, d])
    answer.sort()
    return answer[0]

# stack이용
from collections import defaultdict, deque

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]] # get(a, b)를 하면 routes[a]가 없으면 b를 출력하도록 한다. 디폴트는 None이다.
    for r in routes:
        routes[r].sort(reverse=True)

    print(routes)
    stack = ["ICN"]  
    path = []
    while len(stack) > 0:        
        top = stack[-1]       
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    return path[::-1] #역순 출력

# 스택을 이용한 방식이 훨씬 빨랐다.
# 재귀는 일단 모든 경우를 보다보니 좀 느린편
# 스택부분은 일단 시작지점에 관한 티켓을 다 써야지 등록을 해 버리니 거의 선형시간대에 끝낸듯 하다.