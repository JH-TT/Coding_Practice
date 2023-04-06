from collections import defaultdict

def solution(players, callings):
    cnt = defaultdict(int)
    
    for i, v in enumerate(players):
        cnt[v] = i
    
    for c in callings:
        players[cnt[c]], players[cnt[c]-1] = players[cnt[c]-1], players[cnt[c]]
        cnt[players[cnt[c]]] += 1
        cnt[c] -= 1
    
    return players

# 하나씩 서로 자리를 바꾸는 방식을 이용