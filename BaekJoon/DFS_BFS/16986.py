import sys
from itertools import permutations
input = sys.stdin.readline

n, k = map(int, input().split())

# 좌표를 (1, 1)부터 시작하도록 만듬
info = [[0] * (n + 1)]
for _ in range(n):
    hand = [0] + list(map(int, input().split()))
    info.append(hand)
# 경희, 민호의 손동작을 입력받는다.
kyung = list(map(int, input().split()))
minho = list(map(int, input().split()))

def dfs(a, b, index, wins, P):
    # 지우가 k번 이기면 1을 출력 후 종료.
    if wins[0] == k:
        print(1)
        exit(0)        
    # 경희나 민호중에 우승자가 나오면 현재 함수를 종료시킨다.
    if wins[1] == k or wins[2] == k:
        return 
    # 지우가 모든 손동작을 냈는데도 우승이 없으면 함수를 종료.
    if index[0] == n:
        return

    # 3에서 두 플레이어 합을 빼주면 다음 플레이어가 된다.
    c = 3 - (a + b)

    # 각 플레이어가 낸 손동작
    p1 = P[a][index[a]]
    p2 = P[b][index[b]]

    # 다음으로 낼 손동작 준비
    index[a] += 1
    index[b] += 1
    
    # p1이 이기는 경우
    if info[p1][p2] == 2 or (info[p1][p2] == 1 and a > b):
        wins[a] += 1
        dfs(a, c, index, wins, P)
    # p2가 이기는 경우
    elif (info[p1][p2] == 1 and a < b) or info[p1][p2] == 0:
        wins[b] += 1
        dfs(b, c, index, wins, P)
        
# permutation함수를 이용해 모든 경우의 수를 돌린다.
ziu = list(range(1, n+1))
for i in permutations(ziu, n):
    P = [i, kyung, minho]
    index = [0, 0, 0]
    wins = [0, 0, 0]
    dfs(0, 1, index, wins, P)
print(0)