A = int(input())
T = int(input())
sign = int(input())

line = 2 # 회차 + 1
people = 0 # 사람 수 인데 정확히는 뻔데기 총 단어 개수.
j = 4 # 뻔 or 데기가 한 사이클에 나온 횟수.
h = 8 # 뻔데기 한 사이클돌때 나온 단어개수.
# 뻔 - 데기 - 뻔 - 데기 하고나서 뻔이 line번 데기가 line번 반복됨.
# 그러니 h가 2씩 증가함.
while 1:
    T -= j
    line += 1
    people += h
    if T <= 0:
        T += j
        line -= 1
        people -= h
        break
    j += 1 # 뻔 or 데기의 횟수가 1개씩 늘어남
    h += 2 # 위의 이유로 각각 1개씩 늘어나니 다음 사이클때의 총 단어의 개수는 2개가 증가.

# 남은 단어의 반복 횟수에 따른 답.
if T == 1:
    if sign == 0:
        print(people % A)
    else:
        print((people + 1) % A)
elif T == 2:
    if sign == 0:
        print((people + 2) % A)
    else:
        print((people + 3) % A)
else:
    people += 4
    T -= 2
    if sign == 0:
        print((people + T - 1) % A)
    else:
        people += line
        print((people + T - 1) % A)

# 브루스포스 알고리즘인데 등호같은거 실수해서 시간날린 문제.