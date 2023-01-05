# 2023 카카오 블라인트 코테 1번
import time
from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    d = defaultdict(int)
    today = calc(today, 0)
    for t in terms:
        a, b = t.split()
        d[a] = int(b)

    for i in range(1, len(privacies) + 1):
        t, ty = privacies[i-1].split()
        res = calc(t, d[ty])
        if res <= today:
            answer.append(i)
    
    return answer

def calc(day, m):
    y, month, d = map(int, day.split("."))
    month += m
    return y * 12 * 28 + month * 28 + d

# 전부 일수로 계산해서 비교했음(28일로 통일한 이유인듯?)