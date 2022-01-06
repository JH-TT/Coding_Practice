from itertools import permutations

n, m = map(int, input().split())
arr = [x for x in range(1, n + 1)]
res = set()

for i in permutations(arr, m):
    i = list(i)
    i.sort()
    i = tuple(i)
    res.add(i)
res = sorted(list(res))

for x in res:
    x = list(x)
    print(*x)
# permutation을 이용해서 모든 경우의 수를 구한뒤
# 정렬해주고 중복되는 수열은 한 개로 통일시킨후 출력한다.    