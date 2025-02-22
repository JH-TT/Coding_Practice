from collections import defaultdict

def solution(players, m, k):
    add_rooms = 0
    now_rooms = 0
    rooms = defaultdict(int)

    for t in range(len(players)):
        # 방을 반납한다.
        if t >= k and (t - k) in rooms:
            now_rooms -= rooms[t - k]
        # 현재 인원기준 방이 몇개가 있어야 하는지 미리 구한다.
        suf_rooms = players[t] // m
        if suf_rooms <= now_rooms:
            continue
        add_rooms += (suf_rooms - now_rooms)
        rooms[t] = suf_rooms - now_rooms
        now_rooms = suf_rooms

    return add_rooms

# 그냥 구현문제