def solution(a, b, g, s, w, t):
    answer = 10**16
    left, right = 0, 10**16
    n = len(t)
    
    while left <= right:
        mid = (left + right) // 2
        gold = 0
        silver = 0
        total = 0
        for i in range(n):
            cnt = (mid // t[i] + 1) // 2
            city_gold = min(w[i] * cnt, g[i]) # 현재 시간으로 금을 얼만큼 이동시킬 수 있는지 확인
            city_silver = min(w[i] * cnt, s[i]) # 은도 같은 방식으로 확인
            gold += city_gold
            silver += city_silver
            total += min(s[i] + g[i], w[i] * cnt)
        if gold >= a and silver >= b and total >= a + b:
            right = mid-1
            answer = min(answer, mid)
        else:
            left = mid+1
    
    return answer

# 참고: https://nbalance97.tistory.com/288
# 이분탐색인건 알았지만 어디부분을 잡고해야할지 애매했고 확신이 들지않아서 못푼 문제
# 시간으로 돌리면서 해당 시간에 전부 광물을 옮길 수 있는지 판단하는 문제였다.
# 기존 이분탐색에 구현문제도 섞여 있어서 좀 까다로운 문제였다.