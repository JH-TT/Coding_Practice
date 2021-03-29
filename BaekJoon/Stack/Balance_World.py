while 1:
    array = list(input())
    sub = []
    flag = 0

    if array[0] == ".": # 점만 입력시 종료.
        break

    for i in array: # 전에 풀었던 괄호 짝 맞추기와 거의 같음.
        if i == "(" or i == "[":
            sub.append(i)
        elif i == ")":
            if sub and sub[-1] == "(":
                sub.pop()
            else:
                flag = 1
        elif i == "]":
            if sub and sub[-1] == "[":
                sub.pop()
            else:
                flag = 1
    
    if sub or flag == 1:
        print("no")
    else:
        print("yes")