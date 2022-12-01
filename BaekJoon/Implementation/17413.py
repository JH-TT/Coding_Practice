string = list(input())
answer = ""
sub_s = ""
flag = False
for s in string:
    if s == "<":
        if len(sub_s) > 0:
            answer += " ".join(list(map(lambda x : x[::-1], sub_s.split())))
            sub_s = ""
        answer += s
        flag = True
    elif s == ">":
        answer += s
        flag = False
    else:
        if flag:
            answer += s
        else:
            sub_s += s
if len(sub_s) > 0:
    answer += " ".join(list(map(lambda x : x[::-1], sub_s.split())))
print(answer)