from itertools import combinations
from collections import defaultdict

def solution(relation):
    answer = 0
    status = defaultdict(list)
    col = len(relation[0])
    candidatekey = []

    # 각 분야별로 나누기.
    for i in range(col):
        for j in relation:
            status[i].append(j[i])

    # 1 ~ 칼럼 개수까지 뽑는 모든 경우를 구한다.
    for i in range(1, col + 1):
        combi = list(map(list, combinations(list(range(col)), i)))
        # 후보키를 구한다.
        for j in combi:
            candidate = []
            # 중복되는 내용이 있으면 안넣는다(유일성인지 확인을 위함)
            for k in range(len(relation)):
                can = list(map(lambda x: status[x][k], j))
                if can not in candidate:
                    candidate.append(can)
            # 길이가 같다면 유일성임.
            if len(relation) == len(candidate):
                flag = True
                # 최소성 판단(이미 있는 칼럼들이 포함되면 최소성에 어긋난다. 
                # ex) 학번, 이름이 후보키면 학번,이름,전공이 유일성이어도 최소성은 되지 않음
                for h in candidatekey:
                    cnt = 0
                    for m in h:
                        if m in j:
                            cnt += 1
                    # 유일성 어긋나는 경우 flag를 False로 변경 후 반복문을 탈출한다.
                    if cnt == len(h):
                        flag = False
                        break
                if flag:
                    answer += 1
                    candidatekey.append(j)

    return answer
# 원래 예전부터 풀려고 했던건데 유일성 부분이 이해되지 않아서 남겨뒀던 문제.
# 이해되고나니 문제푸는건 어렵지 않았음.