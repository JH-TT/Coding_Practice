n = int(input())
sq = list(map(int, input().split()))

cnt = [0] * 1000001
s = [0]
ans = [-1] * n

# 각 값들의 출현개수 세기.
for i in sq:
    cnt[i] += 1

for i in range(1, n):
    while s and cnt[sq[s[-1]]] < cnt[sq[i]]:
        idx = s.pop()
        ans[idx] = sq[i]
    s.append(i)

print(*ans)

# 17298 오큰수 문제와 동일. 값의 출현 개수로 오큰수 실행.