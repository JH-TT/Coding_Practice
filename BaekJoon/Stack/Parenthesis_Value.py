array = list(input())
sub = []
sum = 0


for i in array:
    if i == ")":
        s = 0 # 바깥괄호 안에있는 괄호들의 정보.
        while len(sub) != 0:
            top = sub.pop()
            if top == "(": # 맞는 괄호가 나오면
                if s == 0: # 그 괄호안에 다른 괄호가 없었다면.
                    sub.append(2)
                else: # 다른 괄호들이 있었다면 그 괄호들값의 총합에 2를 곱한다
                    sub.append(2 * s)
                break
            elif top == "[": # 맞지않는 괄호면 아웃
                print(0)
                exit(0)
            else:
                s += int(top) # 숫자가 있으면 그 숫자를 s에 저장.(괄호값 정보 저장)

    elif i == "]":
        s = 0
        while len(sub) != 0:
            top = sub.pop()
            if top == "[":
                if s == 0:
                    sub.append(3)
                else:
                    sub.append(3 * s)
                break
            elif top == "(":
                print(0)
                exit(0)
            else:
                s += int(top)
    else:  # "("나 "["는 sub에 넣음
        sub.append(i)

for i in sub:
    if i == "(" or i == "[": # sub에 아직 괄호가 남아있으면 아웃
        print(0)
        exit(0)
    else: # 아닌경우엔 더해나감.
        sum += i
print(sum)