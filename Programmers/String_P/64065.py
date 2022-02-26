# 분리를 안하고 하나씩 보는 방식
def solution(s):
    a = []
    l = []
    s = s[1:-1]
    t = ""
    s_l = []
    for i in range(len(s)):
        if s[i] == "{":
            continue
        elif s[i] == "}":
            s_l.append(int(t))            
            l.append(s_l)
            s_l = []
            t = ""
        elif "0" <= s[i] <= "9":
            t += s[i]
        elif s[i] == ",":
            if s[i+1] == "{":
                continue
            s_l.append(int(t))
            t = ""
 
    l.sort(key=lambda x : len(x)) # -> l.sort(key=len) 으로 해도됨.
    
    for i in l:
        for j in i:
            if j in a:
                continue
            a.append(j)
    
    return a

# 차음부터 분리하고 확인하기
def solution(s):
    a = []
    s = s.lstrip("{").rstrip("}").split("},{")
    l = []
    for i in s:
        l.append(i.split(","))
    
    l.sort(key=len)
    for i in l:
        for j in i:
            if not int(j) in a:
                a.append(int(j))
    
    return a