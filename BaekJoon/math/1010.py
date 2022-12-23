import math

for _ in range(int(input())):
    r, n = map(int, input().split())
    print(int(math.factorial(n) / (math.factorial(r) * math.factorial(n-r))))

# 조합 기본문제