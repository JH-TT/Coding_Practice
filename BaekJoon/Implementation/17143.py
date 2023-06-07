import sys
input = sys.stdin.readline
# 1 : 위, 2 : 아래, 3 : 오른쪽, 4 : 왼쪽
# 정보 : (r, c), 속력, 이동방향, 크기

def move_shark(s):
    cnt = s[2]
    while cnt > 0:
        if s[3] == 1: # 위
            m = min(cnt, s[0]-1)
            cnt -= m
            s[0] -= m
            if s[0] == 1:
                s[3] = 2
        elif s[3] == 2: # 아래
            m = min(cnt, R-s[0])
            cnt -= m
            s[0] += m
            if s[0] == R:
                s[3] = 1
        elif s[3] == 3: #오른쪽
            m = min(cnt, C-s[1])
            cnt -= m
            s[1] += m
            if s[1] == C:
                s[3] = 4
        else:
            m = min(cnt, s[1]-1)
            cnt -= m
            s[1] -= m
            if s[1] == 1:
                s[3] = 3
    return s
  
R, C, M = map(int, input().split())
arr = [[[] for _ in range(C+1)] for _ in range(R+1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c].append([s, d, z])

angler = 0
res = 0
while angler < C:
    # 낚시꾼이 움직인다.
    angler += 1
    # 상어를 잡는다.
    for i in range(1, R+1):
        if len(arr[i][angler]) > 0:
            catch = arr[i][angler].pop()
            res += catch[2]
            break
    # 상어가 움직인다. 
    # 1. 상어들을 회수
    # 2. 상어들을 움직인 후 arr에 넣는다.
    # + 만약 이미 있는 곳에 넣는 경우는 둘 중에 비교해서 잡아먹도록 한다. 
    sharks = []
    for i in range(1, R+1):
        for j in range(1, C+1):
            if len(arr[i][j]) > 0:
                sharks.append([i, j] + arr[i][j].pop())
    for s in sharks:
        move_ = move_shark(s) # 상어를 이동시킨다.
        if len(arr[move_[0]][move_[1]]) == 1:
            shark = arr[move_[0]][move_[1]].pop()
            if shark[2] < move_[4]: # 이번에 오는 상어가 더 크면 잡아먹고 move_상어가 자리를 차지한다.
                arr[move_[0]][move_[1]].append(move_[2:])
            else:
                arr[move_[0]][move_[1]].append(shark)
        else:
            arr[move_[0]][move_[1]].append(move_[2:])
print(res)
# 움직이는 것만 잘 생각하면 쉽게 구현가능했던 문제 (왜 골1이지...)