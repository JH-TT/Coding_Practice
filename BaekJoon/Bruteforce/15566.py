from collections import deque
import sys
input = sys.stdin.readline

def dfs(start, state):
    if start == n+1:
        if check(state):
            print("YES")
            print(*state)
            exit()
        return
      
    for i in graph[start]:
        if i not in state:
            dfs(start+1, state + [i])

def check(s):
    # 1번 연못부터 n번 연못까지
    for i in range(1, n+1):
        # i번 연꽃과 연결된 모든 연꽃정보 (연꽃번호, 취미번호)
        for j in bridge[i]:
            if hobby[s[i-1]][j[1]-1] != hobby[s[j[0]-1]][j[1]-1]:
                return False
    return True

n, m = map(int, input().split())
hobby = [[]]
for _ in range(n):
    hobby.append(list(map(int, input().split())))
graph = [[] for _ in range(n + 1)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    if a == b:
        graph[a].append(i)
    else:
        graph[a].append(i)
        graph[b].append(i)
# 연꽃간의 다리 정보
bridge = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append((b, c))
    bridge[b].append((a, c))

if dfs(1, []) == None:
    print("NO")

# 한동안 못풀어서 냅둔 문제.
# 드디어 맞았다.
# 범위가 넓지 않아서 완전탐색으로 충분히 가능.