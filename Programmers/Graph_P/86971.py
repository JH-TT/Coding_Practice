def solution(n, wires):
    answer = float('inf')
    wires.sort()
    for i in range(n-1):
        parent = list(range(n+1))
        cnt = [0] * (n + 1)
        for j in range(n-1):
            if i == j:
                continue
            union_parent(parent, wires[j][0], wires[j][1])
        for i in range(1, n+1):
            cnt[find_parent(parent, i)] += 1
        num = []
        for i in cnt[1:]:
            if i > 0:
                num.append(i)
        answer = min(answer, abs(num[0] - num[1]))
    
    return answer

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# find_parent와 union_parent를 이용하는 문제. 다만 같은 집합인지 확인하기 위해 find_parent를 자주썼음