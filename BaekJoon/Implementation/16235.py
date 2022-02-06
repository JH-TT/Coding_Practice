# 통과한 코드
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


# 나무번식 범위
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
nutri = [[5] * n for _ in range(n)]
trees = [[deque() for _ in range(n)] for _ in range(n)] # 아무래도 이 부분이 중요했던거 같다.
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    trees[a-1][b-1].append(c)
    ans += 1
    
for i in range(k):
    grown = defaultdict(int)
    # 봄, 여름
    for i in range(n):
        for j in range(n):                        
            length = len(trees[i][j])            
            for k in range(length):
                if trees[i][j][k] <= nutri[i][j]:
                    nutri[i][j] -= trees[i][j][k]
                    trees[i][j][k] += 1
                    if trees[i][j][k] % 5 == 0:
                        grown[(i, j)] += 1
                else:
                    for _ in range(k, length):
                        nutri[i][j] += trees[i][j].pop() // 2
                        ans -= 1
                    break

    # 가을
    for tree in grown:
        for i in range(8):
            nx = tree[0] + dx[i]
            ny = tree[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            for _ in range(grown[tree]):
                trees[nx][ny].appendleft(1)
                ans += 1

    # 겨울
    for i in range(n):
        for j in range(n):
            nutri[i][j] += A[i][j]

print(ans)

# 실패한 코드
import sys
from collections import defaultdict, deque
input = sys.stdin.readline


# 나무번식 범위
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
nutri = [[5] * n for _ in range(n)]
trees = defaultdict(list)
ans = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    trees[(a-1, b-1)].append(c)
    ans += 1

for i in range(k):
    grown = defaultdict(int)
    # 봄, 여름
    for tree in trees:        
        length = len(trees[tree])
        idx = 0
        while trees[tree] and idx < length:
            if nutri[tree[0]][tree[1]] < trees[tree][idx]:
                break
            nutri[tree[0]][tree[1]] -= trees[tree][idx]
            trees[tree][idx] += 1
            if trees[tree][idx] % 5 == 0:
                grown[tree] += 1
            idx += 1
        
        for i in range(idx, length):
            nutri[tree[0]][tree[1]] += trees[tree][i] // 2
            ans -= 1
        trees[tree] = trees[tree][:idx]
    # 가을
    for tree in grown:        
        for i in range(8):
            nx = tree[0] + dx[i]
            ny = tree[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            trees[(nx, ny)] = [1] * grown[tree] + trees[(nx, ny)]            
            ans += grown[tree]

    # 겨울
    for i in range(n):
        for j in range(n):
            nutri[i][j] += A[i][j]

print(ans)

# while문을 for문으로 바꿔준것 뿐인데 통과함.