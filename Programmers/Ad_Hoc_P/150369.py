def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [0] + deliveries
    pickups = [0] + pickups
    
    d_arr = [-1]
    p_arr = [-1]
    
    # 처음 0개 이상인 부분을 각각 구한다.
    for i in range(1, n+1):
        if deliveries[i] != 0:
            d_arr.append(i)
        
    for i in range(1, n+1):
        if pickups[i] != 0:
            p_arr.append(i)
            
    while d_arr[-1] != -1 or p_arr[-1] != -1: 
        answer += max(d_arr[-1], p_arr[-1]) * 2
        d_total = 0
        p_total = 0
        # 운행을 갔다온다.
        while d_arr[-1] != -1:
            if d_total + deliveries[d_arr[-1]] > cap:
                deliveries[d_arr[-1]] -= (cap - d_total)
                break
            d_total += deliveries[d_arr[-1]]
            deliveries[d_arr[-1]] = 0
            d_arr.pop()
        while p_arr[-1] != -1:
            if p_total + pickups[p_arr[-1]] > cap:
                pickups[p_arr[-1]] -= (cap - p_total)
                break
            p_total += pickups[p_arr[-1]]
            pickups[p_arr[-1]] = 0
            p_arr.pop()
    
    return answer

# 그냥 생각해보면 쉬운데 막상 구현하려니 잘 안됐음...