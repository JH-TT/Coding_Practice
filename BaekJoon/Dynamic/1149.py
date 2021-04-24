n = int(input()) # 몇개의 집인지 입력받음.

rst = [] # 결과값 받을 공간.
r, g, b = map(int, input().split())
rst.append((r, g, b)) # 첫번째 집의 RGB입력.
for _ in range(1, n):
    r, g, b = map(int, input().split()) # 현재 집의 RGB입력 받음.
    pR, pG, pB = rst[-1] # 그 전 RGB출력
    # 현재 r + min(이전G, 이전B).
    R = r + min(pG, pB)
    G = g + min(pR, pB)
    B = b + min(pR, pG)
    rst.append((R, G, B))
fR, fG, fB = rst[-1] # 마지막 RGB출력.
print(min(fR, fG, fB)) # 그 중 최솟값 출력.

# 이건 왜 안될까?
n = int(input())

cost = []
result = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

for i in range(3):
    sum = cost[0][i]
    k = i
    for j in range(1, n):
        if k == 0:
            a = min(cost[j][1], cost[j][2])
            sum += a
            k = cost[j].index(a)
        elif k == 2:
            a = min(cost[j][0], cost[j][1])
            sum += a
            k = cost[j].index(a)
        else:
            a = min(cost[j][0], cost[j][2])
            sum += a
            k = cost[j].index(a)
    result.append(sum)
print(min(result))
# 뭔가 다른 경우들을 무시해 버리는 경우가 있는거 같은데 어떤 경우인지 아직 모름..