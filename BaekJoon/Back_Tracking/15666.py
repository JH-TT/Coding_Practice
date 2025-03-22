n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
res = set()

def dfs(a, track, start, cnt):
    global res
    if len(track) == cnt:
        res.add(tuple(track))
        return

    for i in range(max(start, 0), len(a)):
        dfs(a, track + [a[i]], i, cnt)

for i in range(n):
    dfs(arr, [arr[i]], i, m)

res = sorted(list(res))
for r in res:
    print(*r)

# 전형적인 백트래킹 문제
# 다만 리스트가 직접 주어지기 때문에 중복 수열이 발생할 수 있음
# 이런 부분은 집합을 이용해서 해결