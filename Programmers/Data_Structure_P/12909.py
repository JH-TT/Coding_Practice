def solution(s):
    
    stack = []
    
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if not stack:
                return False
            if stack[-1] == "(":
                stack.pop()

    return True if not stack else False

# stack 단골문제...