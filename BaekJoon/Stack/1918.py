import sys
input = sys.stdin.readline

a = list(input().rstrip())

al = []
op = []
flag = False
for i in a:
    if i == "(":
        op.append(i)
    # 닫는 괄호면 열린괄호 전까지 전부 op에서 꺼내서 al에 넣는다.
    elif i == ")":
        while op and op[-1] != "(":
            al.append(op.pop())
        op.pop()
    # *와 /는 +와 -보다 우선순위가 높으니 op안에 */인 것만 꺼낸다.
    elif i == "*" or i == "/":
        while op and (op[-1] == "*" or op[-1] == "/"):
            al.append(op.pop())
        op.append(i)
    elif i == "+" or i == "-":
        while op and (op[-1] != "("):
            al.append(op.pop())
        op.append(i)
    else:
        al.append(i)
while op:
    al.append(op.pop())
print("".join(al))

# 이 문제는 사칙연산의 우선순위도 따져야 하기때문에 좀 까다로웠던 문제.