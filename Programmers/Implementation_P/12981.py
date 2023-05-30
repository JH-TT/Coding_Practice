from collections import defaultdict

def solution(n, words):
    answer = []
    history = defaultdict(int)
    
    for i in range(len(words)):
        # 끝말잇기인지
        if i != 0 and words[i-1][-1] != words[i][0]:
            return [i % n + 1, i // n + 1]
        # 이미 등장한 단어인지
        if history[words[i]]:
            return [i % n + 1, i // n + 1]
        history[words[i]] = 1

    return [0, 0]