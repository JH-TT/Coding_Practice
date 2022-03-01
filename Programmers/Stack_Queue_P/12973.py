def solution(s):
    stack = []
    
    for i in s:
        # stack이 비어있지 않고, 가장 윗 문자와 같으면 pop을 한다.
        if stack and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)

    return 0 if stack else 1 # stack이 안비어있으면 0 아니면 1