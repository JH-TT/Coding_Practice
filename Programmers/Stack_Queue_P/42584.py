# 나의 풀이
def solution(prices):
    answer = []    
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break
        answer.append(cnt)

    return answer
# 그냥 단순 반복문 풀이이다. 그런데 시간복잡도가 O(n^2)가 되기 때문에 좀 찝찝한 풀이    

# 스택을 이용한 풀이
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if stack != []:
            while stack != [] and stack[-1][1] > prices[i]: # 스택의 길이가 1이상이고, 가격이 내려간 상황이면
                past, _ = stack.pop() # top을 뺀다.
                answer[past] = i - past # 얼마나 걸렸는지 놓는다.
        stack.append([i, prices[i]]) # 인덱스와 그 값을 stack에 저장
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer
# 가격이 내려가면, while문을 돌려 stack이라는 따로 보관하는 리스트에서 pop을 해, answer의 값을 수정시킨다.
# pop을해서 하는 이유는 한 번 수정한 인덱스는 더이상 필요가 없기 때문이다.    