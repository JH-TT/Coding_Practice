def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        v1 = calc_dist(m, n, startX, startY, ball[0], ball[1], 1)
        v2 = calc_dist(m, n, startX, startY, ball[0], ball[1], 2)
        v3 = calc_dist(m, n, startX, startY, ball[0], ball[1], 3)
        v4 = calc_dist(m, n, startX, startY, ball[0], ball[1], 4)
        answer.append(min(v1, v2, v3, v4))
    
    return answer

def calc_dist(m, n, a, b, c, d, t):
    total = 0
    if t == 1 and (a != c or b <= d):
        total = (a-c)**2 + (b+d)**2
    elif t == 2 and (a >= c or b != d):
        total = (a-2*m+c) ** 2 + (b-d)**2
    elif t == 3 and (a != c or b >= d):
        total = (a-c)**2 + (b-2*n+d)**2
    elif t == 4 and (a <= c or b != d):
        total = (a+c)**2 + (b-d)**2
    return total if total != 0 else 10**8


# 4가지 중에 최솟값
  # x, y, m, n 축에 각각 쿠션을 해서 맞췄을 때 거리
# 거리를 계산할 때 대칭을 이용해서 풀었다
  # 만약 x축에 쿠션을 해서 맞춘다면 x축에 대칭을 해서 계산