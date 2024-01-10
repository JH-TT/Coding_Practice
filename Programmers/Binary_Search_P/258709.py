from itertools import combinations
from bisect import bisect_left

def solution(dice):
    answer = []
    n = len(dice)
    nums = list(range(1, n + 1))

    wins = 0
    for me in combinations(nums, n // 2):
        me = list(me)
        you = [x for x in nums if x not in me]

        # 자신과 상대방의 모든 경우의 수를 구해놓는다.
        me_all_case = calc(dice, me)
        you_all_case = sorted(calc(dice, you))

        # 이분탐색으로 이긴 횟수를 구한다.
        total_win = 0
        for m in me_all_case:
            total_win += bisect_left(you_all_case, m)

        if total_win > wins:
            answer = me
            wins = total_win

    return answer

# 모든 경우의 수를 구하는 함수
# param: 모든 주사위 정보(dice), 해당되는 주사위 번호리스트(p)
def calc(dice, p):
    start = [0] * len(p) # 현재 더해지는 주사위의 인덱스들
    cases = []
    while True:
        cases.append(sum(dice[j-1][start[i]] for i, j in enumerate(p))) # j-1번째 주사위의 start[i]번째 값
        if start == [5] * len(p): break # 모든 경우를 봤으면 종료

        idx = 0
        while idx < len(p):
            start[idx] += 1
            if start[idx] != 6:
                break
            start[idx] = 0
            idx += 1
    return cases

# 풀이 방식
# 일단 이 문제를 보고 n의 범위가 10인걸 봐서 일단 완탐이긴 하겠다! 라는 느낌이 들었음
# 그래서 내가 나올 수 있는 모든 경우의 수와 상대방이 나올 수 있는 모든 점수들을 하나씩 확인하면서 갱신하는 방식으로 구현. -> 시간초과
# 어디서 시간초과가 나왔나 봤는데, 나와 상대방의 모든 경우의 수를 하나씩 확인하는 부분에서 시간초과가 나왔다.
# 일단 최대 주사위의 개수는 10개이므로 나와 상대방이 가져가는 주사위 최대 개수는 5개가 된다.
# 그리고 각 주사위는 6개의 면이 있으니 내가 5개의 주사위를 가져가서 계산할 수 있는 모든 경우의 수는
# 6^5 = 729개가 된다. 게다가 여기서 상대방의 경우의 수도 확인하니 729^2= 53만대가 나오고 10C5까지 계산하면 터지게 된다.
# 그래서 시간을 줄일 수 있는 방법이 없을까 생각하다가 이분탐색을 떠올렸다.
# 일단 상대방의 모든 경우의 점수를 오름차순으로 정렬한다.
# 그 다음 내 점수를 하나씩 가져와서 이분탐색으로 몇번째로 큰지 확인한다.
# 그 다음은 원래 방식과 같이 진행.
# 이러면 최대 시간복잡도는 53만에서 729 * log(729)로 확 줄어들게 된다.