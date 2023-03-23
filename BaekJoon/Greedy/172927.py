from collections import deque
import copy

def solution(picks, minerals):
    answer = 10**6
    n = len(minerals)
    figure = [[0, 0, 0] for _ in range((n+4) // 5)]
    
    idx = 0
    for i in range(n):
        if minerals[i] == "diamond":
            figure[idx][0] += 1
            figure[idx][1] += 5
            figure[idx][2] += 25
        elif minerals[i] == "iron":
            figure[idx][0] += 1
            figure[idx][1] += 1
            figure[idx][2] += 5
        else:
            figure[idx][0] += 1
            figure[idx][1] += 1
            figure[idx][2] += 1
        if (i+1) % 5 == 0:
            idx += 1
            
    q = deque()
    q.append((picks, 0, 0)) # 현재 곡괭이 정보, 몇 번째 곡괭이 인지, 총 피로도
    
    while q:
        p, i, f = q.popleft()
        if sum(p) == 0 or i >= len(figure):
            answer = min(answer, f)
            continue
        for j in [0, 1, 2]:
            if p[j] == 0:
                continue
            p2 = copy.deepcopy(p)
            p2[j] -= 1
            q.append((p2, i+1, f+figure[i][j]))
    
    return answer

# 광물을 5개씩 묶어서 다이아, 철, 돌 곡괭이일 경우를 구한다.
# 완탐을 돌린다.

# 그리디로 푼 방식
cost_table = {
    "diamond": {
        "diamond": 1,
        "iron": 1,
        "stone": 1,
    },
    "iron": {
        "diamond": 5,
        "iron": 1,
        "stone": 1,
    },
    "stone": {
        "diamond": 25,
        "iron": 5,
        "stone": 1,
    }
}

def calc_cost(minerals):
    diamond_cost, iron_cost, stone_cost = 0, 0, 0
    for mineral in minerals:
        diamond_cost += cost_table["diamond"][mineral]
        iron_cost += cost_table["iron"][mineral]
        stone_cost += cost_table["stone"][mineral]
    return [stone_cost, iron_cost, diamond_cost]


def solution(picks, minerals):
    sum_picks = sum(picks)
    minerals = minerals[:sum_picks*5]
    # 현재 미네랄을 5개로 나눴을때 나오는 구간의 수(5개 미만도 1개로 친다.)
    need_pick_count = len(minerals)//5 + (1 if len(minerals)%5 else 0)
    
    pick_diamond = min(need_pick_count, picks[0])
    pick_iron = min(need_pick_count-pick_diamond, picks[1])
    pick_stone = min(need_pick_count-pick_diamond-pick_iron, picks[2])

    minerals = [calc_cost(minerals[i*5:i*5+5]) for i in range(need_pick_count)]
    minerals.sort() # 돌 기준으로 오름차순

    # 피로도는 돌 -> 철 -> 다이아 순으로 한다.
    # 다이아는 어차피 어떤걸 캐도 1이고, 철은 다이아만 5이다.
    # 돌이 가장 피로도가 많이들기때문에 돌로 먼저 최소한의 다이아, 철을 캐도록 한 뒤
    # 철, 다이아 순으로 간다.
    return sum([
        *[mineral[0] for mineral in minerals[:pick_stone]],
        *[mineral[1] for mineral in minerals[pick_stone:pick_iron+pick_stone]],
        *[mineral[2] for mineral in minerals[pick_iron+pick_stone:]]
    ])

# 현재 광물 상태를 보고 사용할 수 있는 곡괭이를 미리 구해놓는다.(다이아, 철, 돌 순으로)
# 그런다음 구간별로 돌, 철, 다이아로 캤을때 피로도를 구한다.
# 돌 기준으로 오름차순으로 정렬한 뒤(돌이 피로도가 가장 많이들기때문)
# 돌, 철, 다이아 순으로 피로도를 합한다.