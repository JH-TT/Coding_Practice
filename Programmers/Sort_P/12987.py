def solution(A, B):
    answer = 0
    if min(A) >= max(B):
        return 0
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            answer += 1
            i += 1
        j += 1
        
    return answer

# A와 B를 정렬하고 하나씩 확인한다.
# B의 원소가 A보다 크면 둘 다 다음 숫자를 보고
# 그게 아니면 B의 원소만 증가시킨다.