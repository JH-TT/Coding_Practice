import itertools
# itertools라이브러리를 이용하면 아주 쉽게 풀이가능!
# n개의 숫자중에 중복허용x 6개 뽑기 -> Combination 이용.
while(1):
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    b = a[0]
    a.remove(b)
    for x in itertools.combinations(a, 6):
        print(*list(x))
    print()