n = int(input())
shirts = list(map(int, input().split()))
t, p = map(int, input().split())

print(sum(s // t + (s % t > 0) for s in shirts))
print(*divmod(n, p))

# 순회 계산
# 몫, 나머지 연산 문제