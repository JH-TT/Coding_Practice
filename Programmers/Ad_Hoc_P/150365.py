def solution(n, m, x, y, r, c, k):
    answer = ''

    # 목표지점까지 수직거리, 수평거리
    verti = abs(x-r)
    holi = abs(y-c)
    dist = verti + holi
  
    # 최소거리를 제외한 k구하기(왜나면 수직거리 + 수평거리는 목표지점까지의 최소한의 거리이기 때문.)
    k -= dist
    # 만약 최소거리보다도 낮거나, k가 홀수이면 불가능하다.
    # k가 홀수이면 rl 혹은 ud로 움직이는것이 불가능하기 때문
    if k < 0 or k % 2 != 0:
        return "impossible"

    # 각 방향의 개수를 구한다.
    di = {"d":0, "l":0, "r":0, "u":0}
    if x > r:
        di["u"] += verti
    else:
        di["d"] += verti
    if y > c:
        di["l"] += holi
    else:
        di["r"] += holi

    # d가 사전순으로 가장 앞서니 d부터 계산한다.
    answer += "d" * di["d"]
    d = min(int(k/2), n-(x+di["d"])) # n,1 까지 가는 거리와, 남은 k절반(d로 가면 u로 돌아와야하니 절반씩) 중에 최소
    answer += "d" * d
    di["u"] += d # d만큼가면 u로 돌아와야하니 그 값만큼 더해준다.
    k -= 2*d # 갔다오니까 2배

    # 같은 방식
    answer += "l" * di["l"]
    l = min(k//2, y-di["l"]-1)
    answer += "l" * l
    di["r"] += l
    k -= 2*l
    
    answer += "rl" * int(k/2) # rl 추가. (ud보다 사전순으로 앞서기때문)

    # 남은 거리는 r과 u로만 이동. r이 사전순으로 앞서니 r부터 계산한다.
    answer += "r" * di["r"]
    answer += "u" * di["u"]
    
    return answer

# 이 문제를 dfs라고 쉽게 생각하고 도전했다가 평생 못 뻔...
# 문제 해결 전략
# 사전순으로 리턴하기 때문에 최대한 d와 l로 n,1까지 간 뒤, 목표지점으로 가도록 한다.

# 일단 현재 지점에서 목표 지점까지 d, l 또는 u, r 등으로 계산한다.
# 그런다음 최대한 [n, 1] 지점까지 k거리를 넘지 않도록 d, l, r, u 순으로 움직인다.
# 이렇게까지 해도 k가 남는다면 rl 혹은 ud를 추가해준다.
# 왜 lr 또는 du가 아니고 rl, ud인가? -> 시작이 n,1 이기때문에 l혹은 d로 갈 시 범위를 벗어난다.
# 마지막으로 r와 u로 채운다. (n,1 에서 목표지점까지는 r과 u으로만 움직이게 된다.)