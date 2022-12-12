def solution(s):
    cnt = 0 # 시도횟수
    zero_cnt = 0 # 제거된 0개수
    while s != "1": # 0을 계속 제거하기때문에 마지막은 무조건 "1"임.
        cnt += 1 # 횟수 증가.
        zero_cnt += s.count("0") # 제거될 0의 개수 더함
        s = format(s.count("1"), "b") # 1의 개수를 이진수로 변환
    return [cnt, zero_cnt]