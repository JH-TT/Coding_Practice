from collections import defaultdict

def solution(participant, completion):
    cnt = defaultdict(int)
    for p in participant:
        cnt[p] += 1
    for c in completion:
        cnt[c] -= 1
    for c in cnt:
        if cnt[c] != 0:
            return c