def solution(lottos, win_nums):
    answer = []
    cnt = 0
    cnt_zero = lottos.count(0)
    for win in win_nums:
        if win in lottos:
            cnt += 1
    
    return [min(6, 7 - cnt - cnt_zero), min(6, 7 - cnt)]
# 최고등수 : 0을 전부 맞는 숫자로 변경할 경우
# 최저등수 : 0이 win_nums에 없는 숫자로만 변경할 경우