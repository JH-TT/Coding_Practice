import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = []

total = 0
ans = []

for _ in range(m):
    p.append(list(map(int, input().split())))

pT = []
for i in range(n):
    sub = list(p[j][i] for j in range(m))
    pT.append(sub)

for i in range(n):
    pT[i].sort()
    ans.append(pT[i][m // 2])
    for x in pT[i]:
        total += abs(x - ans[-1])
print(total)
print(*ans)

# 맨해튼 거리는 성분 i, j에 대해서 서로 다르면 맨해튼 거리에 영향을 주지 않는다.
# 따라서 line21에 보면 그냥 중간값으로 넣는데 짝수같은 경우는 2개를 봐야하지 않냐라고 생각할 수 있는데
# 첫 번째 주석에 따라서 굳이 볼 필요가 없다.
# 그래서 각 성분마다 중간값을 넣으면서 거리를 계산한다.