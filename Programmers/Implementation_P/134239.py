def solution(k, ranges):
    height = [k]
    area = []
    answer = []
    
    while k != 1:
        if k % 2 == 0:
            k //= 2
            height.append(k)
        else:
            k *= 3
            k += 1
            height.append(k)
    for i in range(1, len(height)):
        area.append(min(height[i], height[i-1]) + ((abs(height[i] - height[i-1])) / 2))
    for f, t in ranges:
        t = len(height) + t - 1
        total = 0.0
        if f > t:
            answer.append(-1.0)
            continue
        for i in range(f, t):
            total += area[i]
        answer.append(total)
    
    return answer

# 단순 구현