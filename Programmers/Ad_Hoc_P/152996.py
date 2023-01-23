from collections import defaultdict

def solution(weights):
    answer = 0
    cnt = defaultdict(int)
    
    for w in weights:
        cnt[w] += 1
    
    weights = sorted(list(set(weights)))
    
    for w in weights:
        if (w*4) % 3 == 0:
            answer += (cnt[w] * cnt[(w*4) // 3]) * ((w*4) // 3 in cnt)
        if (w*4) % 2 == 0:
            answer += (cnt[w] * cnt[w*2]) * (w*2 in cnt)
        if (w*3) % 2 == 0:
            answer += (cnt[w] * cnt[(w*3) // 2]) * ((w*3) // 2 in cnt)
        answer += (cnt[w] * (cnt[w]-1)) // 2
            
    return answer

# 이 문제는 경우의 수가 적고 n의 범위가 넓은 케이스였다.
# 이런 경우는 범위가 큰 것을 타겟으로 잡아서 경우의 수를 따져서 선형탐색으로 끝내는 것이다.
# 푼 방식은
# 각 무게를 for문으로 돌린다.(그 전에 무게들을 오름차순 정렬한다.)
# 오름차순으로 정렬하는 경우는 두 무게의 비율이 2 : 3이면 반대의 경우인 3 : 2도 나올 수 있기 때문에 3 : 2 같은 경우가 나오지 않도록 하는것이다.
# 그러니 나는 4 : 3, 4 : 2, 3 : 2, 같은 경우 총 4가지만 따지면 된다.
# 그런다음 위에 말한 4가지 경우의 수를따지고, 그 수가 리스트에 있는지 확인한 후에 현재 무게의 개수 * 타겟 무게의 개수 를 answer에 더해가면된다.
# 같은 무게는 n*(n-1) / 2로 계산한다.