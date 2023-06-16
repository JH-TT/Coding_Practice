import heapq

def solution(numbers):
    q = []
    heapq.heappush(q, (0, 0, 4, 6)) # 점수, 인덱스, 왼손, 오른손
    all_dict = {}
    all_dict[(4, 6)] = 0 # 점수, 몇번째 인덱스인지

    # 이전 값으로 현재 값을 만들기 때문에 이전 값으로 계속 이어가는 방식은 힘들다. 하려면 몇 번째 숫자로 가는지에 대한 정보도 넣어야 한다. 
    for num in numbers:
        num = int(num)
        cur_dict = {} # 현재번호로 가기 위한 정보들
        for pos, w in all_dict.items():
            l, r = pos
            if l == num:
                if not (num, r) in cur_dict.keys() or cur_dict[(num, r)] > w+1:
                    cur_dict[(num, r)] = w+1
            elif r == num:
                if not (l, num) in cur_dict.keys() or cur_dict[(l, num)] > w+1:
                    cur_dict[(l, num)] = w+1
            else:
                l_p = dp[l][num]
                r_p = dp[r][num]
                if not (num, r) in cur_dict.keys() or cur_dict[(num, r)] > w+l_p:
                    cur_dict[(num, r)] = w+l_p
                if not (l, num) in cur_dict.keys() or cur_dict[(l, num)] > w+r_p:
                    cur_dict[(l, num)] = w+r_p
            all_dict = cur_dict

    return min(list(all_dict.values()))


dx = [0, 1, -1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, -1, 0, -1, -1, 0]

INF = float('inf')
numboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
dp = [[INF] * 10 for _ in range(10)]

# 초기화
for i in range(10):
    dp[i][i] = 1
for i in range(4):
    for j in range(3):
        now = numboard[i][j]
        if now == '*' or now == '#':
            continue
        for h in range(8):
            ni = i + dx[h]
            nj = j + dy[h]
            if ni < 0 or ni >= 4 or nj < 0 or nj >= 3:
                continue
            next_ = numboard[ni][nj]
            if next_ == '*' or next_ == '#':
                continue

            if h in [1, 2, 3, 6]: # 대각선 이동
                dp[now][next_] = 3
            else: # 상하좌우 이동
                dp[now][next_] = 2

# 플로이드 워셜 사용
for k in range(10):
    for a in range(10):
        for b in range(10):
            dp[a][b] = min(dp[a][b], dp[a][k] + dp[k][b])

# 다른 사람 풀이
"""
반드시 하나의 손가락은 이전 숫자를 가리키고 있음을 활용한다.
예를 들어 numbers = "1756"인 경우 2번째로 어느 손가락으로 7을 고를 지 선택하는 상황에서 한 손가락은 반드시 1 위에 있다.
따라서, 반드시 포함하는 숫자는 prevNum으로 보관하고, 다른 숫자가 무엇인지에 대한 최솟값을 dictionary에 보관한다.

예를 들어 15번째 숫자가 5이고, 나머지 숫자에 대한 최솟값이 각각
{0:20, 1:21, 2:22, 3:23, 4:24, 5:MAX, 6:18, 7:19, 8:20, 9:21}이라고 하자.

다음 숫자가 5라면 다음 단계의 결과는 각 값이 1씩 증가한
{0:21, 1:22, 2:23, 3:24, 4:25, 5:MAX, 6:19, 7:20, 8:21, 9:22}가 될 것이며,

다음 숫자가 1이라면
1. (1,5)로 가는 최솟값은 (0,5) 상태에 1과 0 사이의 거리를 더한 값, (2,5) 상태에 1과 2 사이의 거리를 더한 값, ... 중 최솟값이며
2. (1,k) (k!=5)로 가는 최솟값은 (5,k)의 최솟값에 1과 5 사이의 거리를 더한 값이다.
"""

def solution(numbers):
    MAX = 1000000
    defaultMAX = [MAX] * 10
    dist = [[1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
            [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
            [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
            [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
            [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
            [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
            [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
            [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
            [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
            [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]]

    prev = dict(zip(range(10), defaultMAX))
    prev[6] = 0
    prevNum = 4

    for number in numbers:
        number = int(number)
        if number == prevNum:
            for i in range(10):
                prev[i] += 1
            continue
        new = dict(zip(range(10), defaultMAX))
        for i in range(10):
            if i != prevNum:
                new[i] = prev[i] + dist[number][prevNum]
                new[prevNum] = min(new[prevNum], prev[i]+dist[number][i])
        prev = new
        prevNum = number

    return min(prev.values())