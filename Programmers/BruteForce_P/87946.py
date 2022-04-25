from itertools import permutations

def solution(k, dungeons):
    answer = -1
    route = list(range(len(dungeons)))
    for r in permutations(route):
        cnt = 0
        kk = k
        for i in r:
            if dungeons[i][0] <= kk:
                kk -= dungeons[i][1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)
    
    return answer

# 풀이
# 던전을 도는 순서 모든 경우를 permutation을 이용해서 구해놓는다.
# 하나씩 보면서 필요 피로도이상이면 소요 피로도를 뺴주고, 필요 피로도보다 적으면 바로 answer를 업데이트하고 다른 루트를 확인한다.