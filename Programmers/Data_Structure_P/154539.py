from collections import defaultdict

def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)

    return answer

# 간단한 스택문제
# 스택이 비었거나, 해당 숫자가 스택탑에 있는 숫자보다 작으면 넣는다.
# 스택 top에 있는 숫자가 현재 숫자보다 크거나 작을때 까지 계속 꺼낸다.
# 마지막으로 스택에 넣는다.