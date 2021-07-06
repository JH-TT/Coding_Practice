def solution(clothes):
    clothes.sort(key = lambda x : x[1])
    answer = 1
    a = []
    b = []
    while clothes:
        c = clothes.pop(0)
        if not b:
            b.append(c)
        elif b[-1][1] == c[1]:
            b.append(c)
        else:
            a.append(len(b))
            b = []
            b.append(c)
    a.append(len(b))
    for i in a:
         answer *= i + 1
            
    
    return answer - 1
# (종류1개수 + 안입는 경우) * (종류2 개수 + 안입는 경우) 이런식으로 해서 마지막에 아예안입는 경우의 수인 1을 뺴준다.

# 추가 풀이(Counter와 reduce 이용하기))
from collections import Counter
from functools import reduce

# 
def solution(clothes):
    cnt = Counter(x[1] for x in clothes).values()
    answer = reduce(lambda x, y : x * (y + 1), cnt, 1) - 1
    
    return answer