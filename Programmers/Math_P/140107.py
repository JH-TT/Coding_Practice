def solution(k, d):
    same_x = int(d / (2**(0.5) * k))
    answer = (same_x + 1) ** 2
    
    total = 0
    for i in range(same_x*k+k, d+1, k):
        total += (int((d**2 - i**2)**(0.5)) // k + 1)
    
    return answer + total * 2

# y = x 를 하나 그었을때 마지막 x 기준 정사각형내부는 전부 포함
# 그외에 부분은 x를 늘려가면서 확인

# 다른풀이 응용
# 다른풀이를 조금 수정

def solution(k, d):
    c = 0
    for y in range(0, d+1, k): # d까지 이므로 d+1까지.
        x = (d**2 - y**2)**0.5
        c += (x//k + 1) # +1 을 해주는 이유는 x가 0인것도 포함.
    return c

# 그냥 y를 0부터 d까지 k씩 상승시켜 x의 개수를 더해간다.