def solution(num, k):
    res = str(num).find(str(k))
    return res+1 if res != -1 else -1