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

# 규칙을 찾으면 f(n) = 3f(n-2) + 2f(n-4) + ... + 2f(2) + 2 가 나올것이다. --- 1
# 이떄 f(n-2) + f(n-4) = 2f(n-4) + 2f(n-6) + ... 2(2) + 2 가 될것이고
# f(n-2) + f(n-4)를 1번식에 대입하면 f(n) = 4f(n-2) + f(n-4)가 된다.
# 이로써 코드를 옮기게 되는데 그러면 for문이 2개에서 1개로 줄어서 더욱 빨라진다.

# 수정된 코드
def solution(n):
    answer = [0] * 5001
    answer[2] = 3
    answer[4] = 11
    for i in range(6, n+1, 2):
        answer[i] = 4*answer[i-2] - answer[i-4]
    
    return answer[n] % 1000000007