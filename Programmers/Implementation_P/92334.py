from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    bug = defaultdict(list)
    user = defaultdict(int)

    # 중복되는 report도 있어서 미리 중복은 빼고 진행한다.
    report = list(set(report))

    # u: 신고한 유저, target: 신고 당한 유저
    for r in report:
        u, target = r.split()
        bug[target].add(u)
      
    # 신고 당한 유저 리스트를 돌면서 k번 이상 신고받았는지 확인한다.
    # 만약 k번 이상 신고받았다면 해당 유저를 신고한 유저의 value를 1씩 증가시킨다.
    for t in bug:
        if len(bug[t]) >= k:
            for u in bug[t]:
                user[u] += 1
    
    for i in id_list:
        answer.append(user[i])
        
    return answer