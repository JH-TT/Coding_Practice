# 나의 풀이
from collections import defaultdict

def solution(a):
    n = len(a)
    
    if n < 4:
        return 0
        
    answer = 0
    cnt = defaultdict(list)
    
    for i in range(n):
        cnt[a[i]].append(i)
    
    for v in cnt.values():
        if len(v) <= answer // 2:
            continue
        start, end = v[0], v[0]
        l = set()
        for i in v[1:]:
            # 연속된 숫자면 바로 continue
            if end + 1 == i:
                end = i
                continue
            # start가 0이 아닌경우만 start-1을 넣는다.
            if start == 0:
                l.add(end+1)
            else:
                # 1개인 경우
                if start == end:
                    if start-1 in l:
                        l.add(end+1)
                    else:
                        l.add(start-1)
                else:
                    l.add(start-1)
                    l.add(end+1)
            start, end = i, i
        if start != 0:
            if start == end:
                if start-1 in l and end != n-1:
                    l.add(end+1)
                else:
                    l.add(start-1)
            else:
                l.add(start-1)
                if end != n-1:
                    l.add(end+1)
        answer = max(answer, len(l)*2)
        
    return answer

# 다른 사람의 풀이
from collections import defaultdict
def solution(a):
    dic = defaultdict(list)
    for i, v in enumerate(a):
        dic[v].append(i)

    l = len(a)
    answer = 0
    for k, v in dic.items():
        if len(v) <= answer // 2:
            continue
        now = a.copy()
        cnt = 0
        for j in v:
            # 먼저 왼쪽을 채우도록 한다.
            if j > 0 and now[j-1] != k:
                now[j-1] = k
                cnt += 2
            # 그 후에 오른쪽을 채운다.
            elif j < l-1 and now[j+1] != k:
                now[j+1] = k
                cnt += 2
        answer = max(answer, cnt)
    return answer