from itertools import permutations

def m(a):
    sum = 0
    i = 0
    while i < len(a)-1:
        sum += abs(a[i] - a[i + 1])
        i += 1
    return sum

n = int(input())

nums = list(map(int, input().split()))

res = 0
for i in permutations(nums, n):
    res = max(res, m(i))

print(res)