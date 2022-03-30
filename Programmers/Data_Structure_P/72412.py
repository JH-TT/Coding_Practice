import bisect, itertools, collections

def solution(info, query):
    user_info = collections.defaultdict(list)
    bi = list(itertools.product((True, False), repeat = 4)) # "-"가 들어갈 경우들
    
    # 주어진 info에 대해 모든 경우를 구해놓는다.
    for inf in info:
        inf = inf.split()
        for b in bi:
            key = "".join([inf[i] if b[i] else "-" for i in range(4)])
            user_info[key].append(int(inf[4]))
            
    for k in user_info:
        user_info[k].sort()
    
    answer = []
    
    for q in query:
        l, _, p, _, c, _, f, point = q.split()
        key = ''.join([l, p, c, f])
        i = bisect.bisect_left(user_info[key], int(point))
        answer.append(len(user_info[key])-i)
        
    return answer

# 문제의 핵심

# 모든 경우에 대해 구해놓고 key지정 후 점수 삽입
# 점수에 대해 sort
# 각 query에 대해 key와 같이 파싱후 그 key에 대한 점수는 binary search이용해서 몇 개 있는지 탐색