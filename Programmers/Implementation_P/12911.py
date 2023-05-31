def solution(n):
    bi_cnt = bin(n).count('1')
    res = n + 1    
    while True:
        res_cnt = bin(res).count('1')
        if bi_cnt == res_cnt:
            return res
        res += 1
# 반복문을 이용해서 1씩 증가시킨뒤 그 숫자를 2진수로 변경하고 1의 개수를 비교한다.