# 11053(가장 긴 증가하는 부분수열)이랑 똑같음.
n = int(input())
a = list(map(int, input().split()))
v = [1] * n

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            v[i] = max(v[i], v[j] + 1)
print(max(v))