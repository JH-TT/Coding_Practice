# 맞는 괄호인지 판별
def right(s):
    stack = []    
    s = list(s)
    if not s:
        return True      
    if s[0] == ")":
        return False    
    while s:
        a = s.pop(0)
        if not stack:
            stack.append(a)
            continue            
        if stack[-1] + a == "()":
            stack.pop()
        else:
            stack.append(a)            
    if stack:
        return False
    else:
        return True
        

def dfs(s):
    if s == "":
        return ""
    s = list(s)
    a = [0, 0] # 1번은 (, 2번은 )
    u, v = "", ""
    while s:
        b = s.pop(0)
        if b == "(":
            a[0] += 1
        else:
            a[1] += 1
        u += b
        
        if a[0] == a[1]:
            break
    
    v = "".join(s)

    if right(u):
        return u + dfs(v)
    else:
        st = "("
        st += dfs(v)
        st += ")"
        st += "".join(list(map(lambda x : "(" if x == ")" else ")", u[1:-1])))
        return st
        

def solution(p):
    answer = ''    
    if p == "":
        return ""
    if right(p):
        return p
    
    return dfs(p)


# solution함수만으로도 충분히 만들 수 있음.
# 예시
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False # u가 맞는 괄호가 아니면 r을 False로
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))