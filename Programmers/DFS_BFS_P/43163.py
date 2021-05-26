import copy

def dfs(begin, target, words, visit, ans):
    global answer
    for i in range(len(words)):
        cnt2 = 0
        a = copy.deepcopy(visit) # 따로 같은걸 만들어 놔서 계속 for문 돌때마다 넘어온 visit으로 확인하도록 하기.
        if a[i] == 1: # 이미 방문한 단어면 다음 단어로 넘어감.
            continue
        for j in range(len(words[i])):
            if begin[j] != words[i][j]:
                cnt2 += 1
        if cnt2 == 1:
            a[i] = 1
            if words[i] == target:
                answer = min(answer, ans + 1)
                break
            dfs(words[i], target, words, a, ans + 1)
answer = 101 # 전역변수로 해줌.
def solution(begin, target, words):
    global answer

    if target not in words: # 타겟이 words에 없으면 변환을 못하므로 0 리턴.
        return 0
    for i in range(len(words)):
        visit = [0] * len(words) # 이미 확인한 단어는 안봐도 되므로 visit으로 처리.
        cnt = 0 # begin이랑 words[i]와 알파벳 다른 개수.
        ans = 0 # 몇 번 바꿨는지
        for j in range(len(words[i])):
            if begin[j] != words[i][j]:
                cnt += 1
        if cnt == 1:
            visit[i] = 1
            if words[i] == target:
                return 1
            dfs(words[i], target, words, visit, ans + 1) # 조건에 맞는 words[i]가 begin이 되고 나머지는 그대로 넣음.
    
    return answer