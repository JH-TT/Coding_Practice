n = int(input())
consult = [[0, 0] for _ in range(n+2)]
total = [0] * (n+2)

for i in range(1, n+1):
    t, p = map(int, input().split())
    consult[i] = [t, p]

for i in range(1, n+1):
    t, p = consult[i]
    total[i] = max(total[i], total[i-1])
    if i + t > n+1:
        continue
    total[i+t] = max(total[i+t], total[i] + p)
print(max(total[-1], total[-2]))

# 약간 냅색문제 비스무리한 문제