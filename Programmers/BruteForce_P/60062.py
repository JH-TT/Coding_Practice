# 내 코드(시간초과)
from itertools import permutations

def solution(n, weak, dist):
    # dfs(시작노드, 방문 노드, 총 친구, 현재 친구)
    def dfs(cur, res, friend, fixed):
        global answer

        if friend < 0:
            return
        
        if len(fixed) == len(weak) // 2:
            answer = min(answer, res)
            return
        
        for i in range(cur+1, len(weak)):
            if weak[i] - weak[cur] > dist[friend]:
                break
            fixed.add(weak[i] % n)
            if len(fixed) == len(weak) // 2:
                answer = min(answer, res)
                return
        
        for i in range(len(weak) // 2):
            if weak[i] not in fixed:
                dfs(i, res+1, friend-1, fixed | set([weak[i]]))
    
    global answer
    answer = 10**9
    
    for i in range(len(weak)):
        weak.append(n + weak[i])

    for i in range(len(weak) // 2):
        dfs(i, 1, len(dist)-1, set([weak[i] % n]))
    
    return answer if answer != 10**9 else -1

# 해설 코드
from itertools import permutations

def solution(n, weak, dist):
    # complete search
    dist.sort(reverse = True)

    for i in range(1, len(dist)+1):
        permu = list(map(list, permutations(dist[:i], i)))

        for p in permu:
            for start in range(len(weak)):
                # 왼쪽 부분과 오른쪽 부분을 나눈다.
                _left = weak[:start]; _right = weak[start:]
                # 왼쪽 부분은 n을 더해서 오른쪽 부분에 이어붙인다. ex) [1, 5, 6, 10] 에서 시작이 5면 -> [5, 6, 10, 13] 이런식.
                traverse_list = _right + [x+n for x in _left]; candidate = p.copy()
                while traverse_list and candidate:
                    cur = traverse_list.pop(0); d = candidate.pop(0);
                    Cover = cur + d
                    while traverse_list and traverse_list[0] <= Cover: traverse_list.pop(0)

                if not traverse_list:
                    return i
    return -1


# 이 문제의 핵심은 적은 친구를 이용해서 외곽을 전부 수리하는 것이었다.
# 나는 그래서 dist가 아닌 weak을 중심으로 코드를 짰었고 로직은 맞는거 같은데 효율적인 부분에서 시간초과가 떴다.
# 그런데 보니까 dist 즉 친구부분을 위주로 모든 경우의 수(그리디하게)를 찾아서 확인하는 것이었다.
# 최솟값을 찾는 것이기 때문에, 1명으로 할 경우 부터 len(dist)명까지 돌리는 것이다. 이래도 답이 안나오면 -1출력.