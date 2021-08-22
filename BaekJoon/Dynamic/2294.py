import sys
input = sys.stdin.readline
INF = float('inf')

n, k = map(int, input().split())
money = []
for _ in range(n):
    x = int(input())
    if x not in money and x <= k:
        money.append(x)
# money = [i for i in set(int(input()) for _ in range(n)) if i <= k] 이렇게 해도 됨.
money.sort()

ans = [INF] * (k + 1)

for i in money:
    ans[i] = 1
    for j in range(i + 1, k + 1):
        ans[j] = min(ans[j], ans[j - i] + ans[i]) # 현재 j원을 만드는 동전개수와 j - i원을 만드는 개수 + i원 중에 최솟값을 ans[j]로 지정한다.
print(ans[k] if ans[k] < INF else -1) # INF면 -1을 출력 아니면 그 값을 출력

# 비슷한 동전문제를 풀다보니 이젠 감이 잡히는듯 하다.