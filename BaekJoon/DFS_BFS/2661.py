n = int(input())

def dfs(len, a):
    for i in range(1, len // 2 + 1):
        if a[len-(2*i):len-(2*i)+i] == a[len-(2*i)+i:]:
            return

    if len == n:
        # print("".join(map(str, a))) 같은방법.
        print(*a, sep="")
        exit(0)
    for i in range(1, 4):
        if a and a[-1] == i:
            continue
        dfs(len + 1, a + [i])

dfs(0, [])