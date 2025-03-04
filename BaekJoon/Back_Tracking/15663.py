from itertools import combinations, permutations

N, M = map(int, input().split())
seq = list(map(int, input().split()))

ans = set()
if M == 1:
    for i in sorted(seq):
        ans.add(i)

    for i in sorted(list(ans)):
        print(i)
else:
    for case in combinations(seq, M):
        for c in permutations(case, M):
            ans.add(c)

    for i in sorted(list(ans)):
        print(*i)

# 백 트래킹을 유도한거 같은데
# 그냥 조합이랑 순열로 해결