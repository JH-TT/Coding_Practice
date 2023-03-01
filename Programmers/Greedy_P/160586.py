from collections import defaultdict

def solution(keymap, targets):
    answer = []
    keyCount = defaultdict(lambda: 10**5) # 10**5로 초기화
    targets = [list(x) for x in targets] # 문자열을 편리하게 처리하기위해 리스트로 재정의한다.

    # 현재 알파벳을 최소로 누른 횟수
    for key in keymap:
        for i in range(len(key)):
            keyCount[key[i]] = min(keyCount[key[i]], i+1)

    # 이젠 전부 더한다.
    # 만약 총 합이 10**5 이상이면, 찾을 수 없는 알파벳일 있었다는 의미이므로 -1을 넣는다.
    for target in targets:
        total = 0
        for t in target:
            total += keyCount[t]
        if total >= 10**5:
            answer.append(-1)
        else:
            answer.append(total)
    
    return answer