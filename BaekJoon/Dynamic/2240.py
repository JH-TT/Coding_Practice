t, w = map(int, input().split())

tree = []
for _ in range(t):
    tree.append(int(input()))

# T[어느나무][몇초][몇번움직였는지]
T = [[[0] * 33 for _ in range(1010)] for _ in range(2)]
if tree[0] == 1:
    T[0][1][0] = 1
else:
    T[1][1][1] = 1

result = 0

for i in range(2, t + 1):
    for j in range(w + 1):
        if tree[i - 1] == 1:
            # 같은 나무(같은나무에 그대로 있거나, 다른나무에서 넘어오거나)
            T[0][i][j] = max(T[0][i][j], T[0][i - 1][j] + 1)
            T[0][i][j] = max(T[0][i][j], T[1][i - 1][j - 1] + 1)

            # 다른 나무(그냥 그대로 있음, 다른나무에서 넘어옴)
            T[1][i][j] = max(T[1][i][j], T[1][i - 1][j])
            T[1][i][j] = max(T[1][i][j], T[0][i - 1][j - 1])
        else:
            # 다른 나무
            T[0][i][j] = max(T[0][i][j], T[0][i - 1][j])
            T[0][i][j] = max(T[0][i][j], T[1][i - 1][j - 1])

            # 같은 나무
            T[1][i][j] = max(T[1][i][j], T[1][i - 1][j] + 1)
            T[1][i][j] = max(T[1][i][j], T[0][i - 1][j - 1] + 1)

for i in range(w + 1):
    result = max(result, T[0][t][i])
    result = max(result, T[1][t][i])
print(result)