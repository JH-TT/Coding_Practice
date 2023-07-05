# 내 풀이
def solution(s):
    answer = []
    
    for i in range(len(s)):
        target = s[i]
        if len(target) < 4:
            answer.append(target)
            continue
        b = ""
        stack = []
        idx = 0
        zero = -1
        while idx < len(target):
            if not stack:
                if target[idx:idx+3] == "110":
                    idx += 3
                    b += "110"
                else:
                    stack.append(target[idx])
                    if target[idx] == "0":
                        zero = len(stack)-1
                    idx += 1
            else:
                if target[idx:idx+3] == "110":
                    idx += 3
                    b += "110"
                elif stack[-1] == "1" and target[idx:idx+2] == "10":
                    idx += 2
                    b += "110"
                    stack.pop()
                elif stack[-2:] == ['1', '1'] and target[idx] == "0":
                    idx += 1
                    b += "110"
                    stack.pop()
                    stack.pop()
                else:
                    stack.append(target[idx])
                    if target[idx] == "0":
                        zero = len(stack)-1
                    idx += 1
        target = "".join(stack)
        if zero == len(target)-1:
            answer.append(target + b)
        else:
            answer.append(target[:zero+1] + b + target[zero+1:])
        
    return answer

# 좀 깔끔한 풀이
def f(n):
    stk = []
    cnt = 0
    for i in n:
        stk.append(i)
        if i == '0' and stk[-3:] == ['1', '1', '0']:
            del stk[-3:]
            cnt += 1
    idx = -1
    for i in range(len(stk)):
        if stk[i] == '0':
            idx = i
    if idx < 0:
        ret = "110"*cnt + ''.join(stk)
    else:
        ret = ''.join(stk[:idx+1]) + "110"*cnt + ''.join(stk[idx+1:])
    return ret
def solution(s):
    return [f(x) for x in s]

# 이 문제는 110을 적절하게 옮겨서 사전 순으로 가장 앞에 오도록 하는 문제다.
# 최대한 사전 순으로 앞에 오도록 하려면
# 1. 가장 뒤에 있는 0바로 뒤에 붙어야 한다.
# 2. 찾은 110보다 뒤에있는 부분이 더 앞서면 당긴다.
# 등등....
# 이 두 가지를 생각해보면 나오는 결론이 110을 전부 뺀 뒤, 가장 멀리있는 0바로 뒤에 붙이면 된다.
# 파이썬이면 분명 슬라이싱을 사용할 텐데
# 슬라이싱보다 del이 훨씬 빠르다는걸 느꼈다.ㅜㅜ del은 반환하지 않기 때문이다. 
# 이걸 몰랐던 나는 슬라이싱을 사용하지 않고 풀었다. 