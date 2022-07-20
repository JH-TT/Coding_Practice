a, b = map(int, input().split())
c = int(input())

total_minute = a*60 + b + c
h = (total_minute // 60) % 24
m = total_minute % 60
print(h, m)

# 기본적인 시간문제