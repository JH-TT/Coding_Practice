from collections import defaultdict

def solution(cookie):
    answer = 0
    MAX = sum(cookie) // 2
    acul = [0] * (len(cookie) + 1)
    for i in range(len(cookie)):
        acul[i+1] += cookie[i] + acul[i]

    pos = defaultdict(set)
    check = defaultdict(lambda: False)

    for left in range(1, len(cookie) + 1):
        for right in range(left, len(cookie) + 1):
            aSum = acul[right] - acul[left-1]
            if aSum <= answer or check[aSum]: continue
            if left > 1 and len(pos[left-1]) > 0:
                if aSum in pos[left-1]:
                    answer = max(answer, aSum)
                    check[aSum] = True
                    continue
            pos[right].add(aSum)

    return answer

# right를 키 값으로 두고, right값까지 나올수 있는 모든 구간합을 구해놓는다.
# left - 1의 값들을 보면서 aSum값이 있으면 answer를 갱신해 준다.
# 반복



# 로직은 비슷하지만 훨씬 간결한 코드
from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer

# a는 m까지의 모든 누적합을 구한다. (그냥 구하는것이 아닌, 반대로 뒤집어서 left부터 빼면서 확인할 수 있도록 한다.)
# b는 m+1부터 모든 누적합을 구한다.
# a & b를 하면 공통되는 숫자들의 집합이 된다.
# 거기에 answer까지 추가해 가장 큰 값을 answer로 지정한다.



# 총평
# 아래코드와 비교하면 로직은 같지만, 아래코드자체가 훨씬 보기 좋았다.
# 추가로... accumulate가 for문보다 더 빠르다고 한다.