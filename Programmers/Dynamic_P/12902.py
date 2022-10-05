def solution(n):
    answer = [0] * 5001
    answer[2] = 3
    answer[4] = 11
    answer[6] = answer[2] * 2 + answer[4] * 3 + 2
    for i in range(8, n+1, 2):
        answer[i] = answer[i-2] * 3
        for j in range(i-4, 0, -2):
            answer[i] += answer[j] * 2
        answer[i] += 2

    return answer[n] % 1000000007

# 백준에서 풀었던 기억이 있었다.
# 내풀이를 좀 더 간단하게 정리한것이다. https://school.programmers.co.kr/questions/35882

# 수정된 코드
def solution(n):
    answer = [0] * 5001
    answer[2] = 3
    answer[4] = 11
    for i in range(6, n+1, 2):
        answer[i] = 4*answer[i-2] - answer[i-4]
    
    return answer[n] % 1000000007