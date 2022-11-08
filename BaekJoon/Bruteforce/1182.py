def dfs(idx, total):
    global cnt
    if total == s:
        cnt += 1
      
    for i in range(idx+1, n):
        dfs(i, total+seq[i])

n,s = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0

for i in range(n):
    dfs(i, seq[i])
print(cnt)