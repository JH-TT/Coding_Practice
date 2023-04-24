def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = divmod(i, n)
        if col < row+1:
            answer.append(row+1)
        else:
            answer.append(col+1)
        
    return answer

# 몫과 나머지를 이용해서 푸는 문제였다.