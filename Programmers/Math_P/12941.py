def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a, b in zip(A, B):
        answer += a * b

    return answer

# 각 원소끼리 곱해서 더한값이 제일 작게 나오도록 하는 문제
# 그냥 하나는 오름차순, 다른 하나는 내림차순으로 정렬하고 구하면됨.

# 더 짧게 구현해볼 수 있다.
def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum(map(lambda x : x[0] * x[1], zip(A, B)))

# 한 줄로 표현가능하다.
def solution(A,B):
    return sum(map(lambda x : x[0] * x[1], zip(sorted(A), sorted(B, reverse=True))))