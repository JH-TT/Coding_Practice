def solution(money):
    n = len(money)
    answer = [[money[i], money[i]] for i in range(n)]
    answer[0][1] = 0
    answer[1][0] = 0
    answer[2][0] += answer[0][0] # 3번째는 1번째집이랑 합칠 수 있으니 미리 업데이트
    
    # 4번쨰부터는 1번째 집을 거친 경우, 안거친 경우로 나눈다.
    for i in range(3, n):                
        answer[i][0] = max(answer[i][0], money[i] + max(answer[i-2][0], answer[i-3][0]))
        answer[i][1] = max(answer[i][1], money[i] + max(answer[i-2][1], answer[i-3][1]))
    
    # 가장 마지막집은 1번인덱스만, 그 외에는 0, 1 인덱스값을 가지고 이중에 가장 큰 값을 리턴한다.
    return max(max(max(x) for x in answer[:-1]), answer[-1][1])