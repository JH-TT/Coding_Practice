from collections import defaultdict

def solution(s):
    answer = [-1] # 첫번째 알파벳은 무조건 -1이니 미리 초기화 한다.
    cnt = defaultdict(lambda: -1) # 좀 더 편리하게 처리하기 위해 -1로 초기화 한다.
    cnt[s[0]] = 0 # 첫번째 알파벳은 0으로 초기화
    for i in range(1, len(s)): # 첫번째는 이미 처리했으니 1부터 시작
        if cnt[s[i]] == -1:
            answer.append(-1)
            cnt[s[i]] = i
        else:
            answer.append(i - cnt[s[i]])
            cnt[s[i]] = i
        
    return answer