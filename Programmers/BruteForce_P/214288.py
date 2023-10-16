from itertools import combinations
import heapq

def solution(k, n, reqs):
    answer = float('inf')
    cri = list(range(1, n))

    for com in combinations(cri, k-1):
        cnt = [0] * (k+1)
        com = [0] + list(com) + [n] # [0, 1, 2, 3]
        for i in range(1, k+1):
            cnt[i] = com[i] - com[i-1]

        res = 0
        hp = [[] for _ in range(k+1)]
        for req in reqs:
            # 남은 상담사가 있으면 그대로 상담시작
            if len(hp[req[2]]) < cnt[req[2]]:
                heapq.heappush(hp[req[2]], req[0] + req[1]) # 끝나는 시간 저장
                continue
            # 만약 상담사가 꽉 찼으면...
            first = heapq.heappop(hp[req[2]]) # 가장 먼저 끝나는 사람을 꺼낸다.
            res += max(first - req[0], 0) # 만약 해당 사람이 이미 끝난거면 0이 되도록 한다.
            heapq.heappush(hp[req[2]], max(first, req[0]) +req[1]) # 새로운 참가자를 넣어준다.

        answer = min(answer, res) # 둘 중 더 최솟값을 업데이트

    return answer

# 이 문제는 시간복잡도를 계산해 보면 충분히 완탐으로 된다는 것을 알 수 있다.
# n명의 멘토중 k개의 유형이 있다. ---> o ! o ! o ! o ! o
# 느낌표 중에 k-1개를 선택해서 경계를 나누면 된다. (유형당 최소 1명은 있어야 하니 바깥쪽은 필요없다)
# 그러면 n-1Ck-1이 되고, 아무리 커봐야 19C4 -> 3876이고 reqs의 크기는 300이니
# 3876 * 300 은 백만을 조금 넘는 정도이다.

# 그래서 멘토가 나올 수 있는 모든 경우를 구한뒤, reqs를 하나씩 살핀다.
# 지금온 참가자 유형의 멘토가 아직 남아있으면 상담진행
# 만약 꽉 찼다면 가장 먼저 끝나는 사람을 꺼내서 시간비교후 상담시작
# "가장 먼저 끝나는" -> heap을 이용해서 넣는다. 이때 상담하는 사람이 "끝나는 시간"을 넣어준다.
# 하나씩 보면서 answer를 업데이트 해주면 끝.