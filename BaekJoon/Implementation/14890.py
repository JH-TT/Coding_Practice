import sys
input = sys.stdin.readline

n, l = map(int, input().split())

row = [list(map(int, input().split())) for _ in range(n)]
cul = []
cnt = 2 * n

row2 = []
cul2 = []

for i in range(n):
    arr = []
    for j in range(n):
        arr.append(row[j][i])
    cul.append(arr)

for i in row:
    r = i[0]
    r_cnt = 1
    row3 = []
    for j in i[1:]:
        if j == r:
            r_cnt += 1
        else:
            row3.append((r, r_cnt))
            r = j
            r_cnt = 1
    row3.append((r, r_cnt))
    row2.append(row3)

for i in cul:
    c = i[0]
    c_cnt = 1
    cul3 = []
    for j in i[1:]:
        if j == c:
            c_cnt += 1
        else:
            cul3.append((c, c_cnt))
            c = j
            c_cnt = 1
    cul3.append((c, c_cnt))
    cul2.append(cul3)

for i in row2:
    print(i)
print()
for j in cul2:
    print(j)

for i in row2:
    flag = i[0][0]
    flag_cnt = i[0][1]
    for j in range(1, len(i)):
        if abs(flag - i[j][0]) > 1: #1 높이가 2이상 차이나면 경사로 못 놓음.
            cnt -= 1
            break
        elif flag < i[j][0] and flag_cnt < l: #2 다음 수가 더 크고, 현재 수의 개수가 l보다 작으면 경사로 못 놓는다.
            cnt -= 1
            break
        elif flag > i[j][0]: #3 다음 수보다 크고, 다음수의 개수가 l보다 작으면 경사로 못 놓는다.
            if i[j][1] < l:
                cnt -= 1
                break
            elif i[j][1] < 2 * l and j + 1 < len(i) and i[j+1][0] >= flag: #4 경사로는 1개 놓을 수 있지만 앞뒤로 높은 벽이면 안됨.
                cnt -= 1
                break
        flag = i[j][0]
        flag_cnt = i[j][1]
for i in cul2:
    flag = i[0][0]
    flag_cnt = i[0][1]
    for j in range(1, len(i)):
        if abs(flag - i[j][0]) > 1: #1 높이가 2이상 차이나면 경사로 못 놓음.
            cnt -= 1
            break
        elif flag < i[j][0] and flag_cnt < l: #2 다음 수가 더 크고, 현재 수의 개수가 l보다 작으면 경사로 못 놓는다.
            cnt -= 1
            break
        elif flag > i[j][0]: #3 다음 수보다 크고, 다음수의 개수가 l보다 작으면 경사로 못 놓는다.
            if i[j][1] < l:
                cnt -= 1
                break
            elif i[j][1] < 2 * l and j + 1 < len(i) and i[j+1][0] >= flag: #4 경사로는 1개 놓을 수 있지만 앞뒤로 높은 벽이면 안됨.
                cnt -= 1
                break
        flag = i[j][0]
        flag_cnt = i[j][1]
print(cnt)
# 접근 방법 : 인접한 같은수끼리 개수로 묶고서 조건에 따라 작동하도록 했다.
# ex) [1, 1, 1, 3, 2] 이런식이면 -> [(1, 3), (3, 1), (2, 1)] 더 보기 쉽게 바꿈.
# 단점은 리스트를 3개나 사용해서 메모리가 비효율적으로 사용됨. 다른 사람들은 2만대후반 이었는데 나는 3만대 초반이 떴다.