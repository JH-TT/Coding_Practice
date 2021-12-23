from itertools import permutations

n, m = map(int, input().split())
arr = [x for x in range(1, n + 1)]

if m > 1:
    arr = list(permutations(arr, m))
    arr.sort()

    for i in arr:
        print(*i)
else:
    for i in arr:
        print(i)

# n과 m이 최대 8까지이므로 permutation을 이용해서 m개 선택한 경우를 모두 구한 후 정렬하고 출력한다.