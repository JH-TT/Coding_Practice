from itertools import combinations

def solution(n, q, ans):
    global res

    # i번째 힌트, 숫자 후보들, 후보가 되면 안되는 숫자들
    def dfs(i, a, b):
        global res
        # 마지막까지 잘 끝냈다면
        if i == len(q):
            remain = set(list(range(1, n + 1))) - a - b
            a = list(a)
            b = list(b)
            if len(a) == 5:
                res.append(a)
            elif  len(a) < 5 and len(remain) >= 5 - len(a):
                for c in combinations(remain, 5 - len(a)):
                    c = list(c)
                    res.append(sorted(a + c))
            return

        choose = ans[i] # 선택해야하는 개수

        target = set(q[i]) & a # 현재 타겟이 된 숫자들
        not_target = (set(q[i]) - a) - b  # 후보가 될 숫자들
        if len(target) > choose: # 이미 choose의 개수를 넘기면 실패!
            return

        if len(target) == choose: # 같으면 바로 다음 힌트로 넘어감
            dfs(i + 1, a, b | not_target)
            return

        choose -= len(target)

        for case in combinations(not_target, choose):
            case = set(case)

            dfs(i + 1, a | case, b | (not_target - case))

    res = []
    dfs(0, set(), set())
    return len({tuple(sorted(x)) for x in res})

# 직접 다 확인해서 구하는걸 했는데
# 생각해보니 숫자는 아무리많아봐야 30개고 이 중에 5개의 암호만 맞추면 되는거니 nC5의 모든 상황을 가져와서 각각 q리스트마다 힌트의 개수가 맞는지 역으로 확인하면 된다.
# 아래는 그 코드이다.
from itertools import combinations

def solution(n, q, ans):
    answer = 0

    # 1 ~ n까지 5개를 뽑는 모든 경우를 가져온다.
    for case in combinations(list(range(1, n + 1)), 5):
        flag = True
        # q를 하나씩 보면서
        for i in range(len(q)):
            # hit 개수가 다르면 flag를 False로 세팅하고 해당 loop escape.
            if len(set(case) & set(q[i])) != ans[i]:
                flag = False
                break
        # flag가 True면 조건에 부합한 case이므로 answer 1 증가.
        if flag:
            answer += 1

    return answer