from collections import defaultdict

def move(cor, dir):
    if dir == 0:
        return [cor[0] - 1, cor[1]]
    if dir == 1:
        return [cor[0] - 1, cor[1] + 1]
    if dir == 2:
        return [cor[0], cor[1] + 1]
    if dir == 3:
        return [cor[0] + 1, cor[1] + 1]
    if dir == 4:
        return [cor[0] + 1, cor[1]]
    if dir == 5:
        return [cor[0] + 1, cor[1] - 1]
    if dir == 6:
        return [cor[0], cor[1] - 1]
    if dir == 7:
        return [cor[0] - 1, cor[1] - 1]

def solution(arrows):
    answer = 0
    # 튜플은 키값으로 된다.
    cor = defaultdict(lambda: [0 for _ in range(8)])
    visit = defaultdict(int)

    pos = [0, 0]
    visit[tuple(pos)] = 1

    for ar in arrows:
        # 1 x 1 사각형의 경우 서로 대각선으로 움직이면 도형 개수를 세기 힘들다
        for _ in range(2):
            nxt = move(pos, ar)
            if visit[tuple(nxt)] and cor[tuple(pos)][ar] == 0:
                answer += 1
            cor[tuple(pos)][ar] = 1
            pos = nxt
            visit[tuple(pos)] = 1
            cor[tuple(pos)][(ar + 4) % 8] = 1

    return answer

# 주어진 방향대로 움직이다가 이미 지난 점을 처음으로 만날때 방의 개수 + 1을 하는 방식
# 오일러 다면체 정리라고 있는데 그걸로도 해결 가능.