def solution(s):
    s2 = list(map(int, s.split()))
    return str(min(s2)) + " " + str(max(s2))

# min과 max를 이용해서 푸는 문제.