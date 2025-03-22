n, m = map(int, input().split())

# 백트래킹 이용하기

def dfs(track, maxi, cnt):
    if len(track) - 1 == cnt:
        print(*track[1:])
        return

    for i in range(max(track[-1], 1), maxi + 1):
        dfs(track + [i], maxi, cnt)


dfs([0], n, m)

# 백트래킹으로 해결
# itertools의 combinations_with_replacement을 이용하면 간단하게 풀 수 있지만 문제의 요점은 백트래킹을 의도했기에 백트래킹으로 해결