from collections import Counter

file = []
for _ in range(int(input())):
    file.append(input().split(".")[1])

f = list(Counter(file).items())
for i in sorted(f):
    print(*i)

# 파이썬이라 Counter로 금방끝났던 문제. 하지만 n의 범위가 좀만 높아져도 시간초과가 뜰 거 같음.