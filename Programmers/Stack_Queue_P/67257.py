from itertools import permutations

def cal(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b

def solution(expression):
    answer = 0
    a = ["+", "-", "*"]
    
    e = expression
    e = e.replace("+", " ")
    e = e.replace("-", " ")
    e = e.replace("*", " ")
    e = e.split()
    num = [int(n) for n in e]
    
    oper_split = [op for op in expression if not op.isdecimal()]
    
    for i in permutations(a):
        _num = num
        _oper = oper_split
        for j in range(3):
            stack_num = []
            stack_oper = []
            stack_num.append(_num[0])
            
            for k in range(len(_oper)):
                stack_num.append(_num[k+1])
                stack_oper.append(_oper[k])
                
                if stack_oper[-1] == i[j]:
                    num1 = stack_num.pop()
                    num2 = stack_num.pop()
                    op = stack_oper.pop()
                    stack_num.append(cal(num2, num1, op))
            
            _num = stack_num
            _oper = stack_oper
        answer = max(answer, abs(_num[0]))
    
    return answer

# 숫자와 연산자를 따로 나눠서 리스트로 저장한다.
# 숫자와 연산자를 번갈아 넣으면서 계산해야할 연산자면 계산 후 넣는다.

# 다른 사람의 풀이
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

# 그냥 각 상황마다 괄호를 씌우고 eval함수로 계산한 것.