n = int(input())

ans = [[] for _ in range(7)] # 정답 넣을 공간.

def div(l, r, cnt):  
    if cnt == 7:
        return    
    
    mid = (l + r) // 2 # 중간인덱스를 구한다.

    for i in range(l, mid): # 처음 ~ 중간 이전 : A를 추가한다.
        ans[cnt] += "A"
    
    for j in range(mid, r): # 중간 ~ 마지막 : B를 추가한다
        ans[cnt] += "B"

    # 또 다음 절반을 이어간다.
    div(l, mid, cnt + 1)
    div(mid, r, cnt + 1)

div(0, n, 0)

s = "" # cnt가 7이 될 동안 더 이상 절반으로 쪼개지지 않은 경우 나오는 문자열
temp = "" # s랑 같은 문자열이면 대신 출력할 문자열(처음만 A 나머지는 B)

for i in range(n):
    s += "B"
    if i == 0:
        temp += "A"
    else:
        temp += "B"

for i in range(7):
    if "".join(ans[i]) == s:
        print(temp)
    else:
        print("".join(ans[i]))

# 처음 접해봐서 그런지 많이 헷갈렸다. 거의 감도 안왔었음.