def a(num, s, idx, n):
    global max_s, min_s

    if idx == k:
        max_s = max(max_s, s)
        min_s = min(min_s, s)
        return
    # < 면 n보다 큰 수를 돌린다. 반대면 작은수를 돌린다.
    if inequality[idx] == "<":
        for i in range(n+1, 10):
            if num[i] != 1:
                num[i] = 1
                a(num, s+str(i), idx+1, i)
                num[i] = 0
    else:
        for i in range(n-1, -1, -1):
            if num[i] != 1:
                num[i] = 1
                a(num, s+str(i), idx+1, i)
                num[i] = 0


number = [0] * 10

k = int(input())
max_s = "0" * (k+1)
min_s = "9" * (k+1)
inequality = list(input().split())

for i in range(10):
    number[i] = 1
    a(number, str(i), 0, i)
    number[i] = 0

print(max_s)
print(min_s)