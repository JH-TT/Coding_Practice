# BFS
from collections import deque

answer = 0

def bfs(numbers, target, a, s):
    global answer
    q = deque()
    q.append((a, s))
    while q:
        a, s = q.popleft()
        if a + 1 == len(numbers): # 마지막 인덱스고 타겟이랑 값이 같으면 answer에 1을 더함.
            if s == target:
                answer += 1
            continue
        q.append((a + 1, s + numbers[a + 1]))
        q.append((a + 1, s - numbers[a + 1]))

def solution(numbers, target):
    global answer
    bfs(numbers, target, 0, numbers[0])
    bfs(numbers, target, 0, -numbers[0])
    
    
    return answer

# 재귀(슬라이싱 이용)
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# count이용
def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)