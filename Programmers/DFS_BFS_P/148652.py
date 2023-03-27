def solution(n, l, r):
    answer = 0
    level_one = [1, 1, 0, 1, 1]
    one_cnt = [4**i for i in range(21)]
    
    num = 5 ** (n - 1)
    c = 0
    
    if n == 1:
        return level_one[l-1:r].count(1)
    
    for i in range(5):
        c += num
        if l <= c:
            start = [l-c+num, min(num, r-c+num)]
            start_idx = i
            c = 0
            break
    for i in range(5):
        c += num
        if r <= c:
            end = [max(l-i*num, 1), r-c+num]
            end_idx = i
            break
    # 중간
    for i in range(start_idx+1, end_idx):
        if i == 2:
            continue
        answer += one_cnt[n-1]
    
    answer += solution(n-1, start[0], start[1]) if start_idx != 2 else 0
    if (start_idx != end_idx) and end_idx != 2:
        answer += solution(n-1, end[0], end[1])
    
    return answer

# 11011 11011 00000 11011 11011 n=2인 유사 칸토어 비트열이다.
# 5개를 하나의 그룹으로 보고 각 그룹을 인덱스로 보게되면
# l부분이 있는 그룹은 start인덱스, r부분이 있는 그룹은 end인덱스로 보고
# l이 있는 그룹과 r이 있는 그룹 사이는 전부 1을 세주고
# start와 end는 또 재귀함수를 돌려서 level을 1감소시켜서 개수를 세 준다.


# 다른 풀이
def solution(n, l, r):
    answer = r-l+1
    for num in range(l-1,r):
        while num>=1:
            a,b=divmod(num,5)
            if b==2 or a==2:
                answer-=1
                break
            num=a


    return answer
# 근데 이 풀이는 이중반복문이라 많이 느리다.