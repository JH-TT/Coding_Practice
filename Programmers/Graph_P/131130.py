from collections import defaultdict, Counter

def solution(cards):
    cycle = [0] * (len(cards) + 1)
    c = 1
    for i in range(len(cards)):
        if cycle[cards[i]]:
            continue
        idx = cards[i]
        while cycle[idx] == 0:
            cycle[idx] = c
            idx = cards[idx-1]
        c += 1
    res = sorted(list(Counter(cycle[1:]).values()), reverse=True)
    
    return res[0] * res[1] if len(res) != 1 else 0

# cards에서 사이클을 찾고 각 사이클 그룹개수 기준 내림차순으로 정렬한 뒤, Top2를 서로 곱해서 리턴하면된다.
# 만약 cards자체가 하나의 그룹이되면 2번그룹은 0개니까 답이 0이되어야 한다. (그냥하면 res[1]부분에서 런타임 에러 발생함)