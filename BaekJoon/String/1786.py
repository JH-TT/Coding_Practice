T = input()
P = input()
cnt = 0
pos = []

table = [0 for _ in range(len(P))]

j = 0
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = table[j-1]
    if P[i] == P[j]:
        j += 1
        table[i] = j

j = 0
for i in range(len(T)):
    # 만약 다른 문자열이면 어디까지 일치했는지 확인후, 그 위치 이후로 이동.
    while j > 0 and T[i] != P[j]:
        j = table[j-1]
    if T[i] == P[j]:
        if j == len(P)-1:
            cnt += 1
            pos.append(i-len(P)+2)
            j = table[j]
        else:
            j += 1
print(cnt)
print(*pos)

# KMP 기본문제.