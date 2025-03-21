import sys, math
input = sys.stdin.readline

INF = 1000000007

# 분할정복을 이용한다.
def find_inverse(i, exp):
    if exp == 1:
        return i

    if exp % 2 == 0:
        half = find_inverse(i, exp // 2)
        return half * half % INF

    return i * find_inverse(i, exp - 1) % INF

m = int(input())
total = 0

for _ in range(m):
    n, s = map(int, input().split())
    if s % n == 0:
        total += s // n
        continue

    # 기약분수로 만든다.
    g = math.gcd(s, n)
    n //= g
    s //= g

    total += s * find_inverse(n, INF - 2) % INF
    total %= INF

print(total)