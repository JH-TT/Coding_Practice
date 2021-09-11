import sys
input = sys.stdin.readline

n, k = map(int, input().split())

a = [0] * n
num = [0] * n
m = list(map(int, input().split()))
q = int(input())

# 각 jump들이 몇 번 호출됐는지 체크
for i in m:
    num[i] += 1

# 에라토스테네스 비스무리하게 jump만큼 돌면서 a[j]에 jump호출 횟수만큼 더한다.
for i in range(n):
    if num[i] != 0:
        for j in range(0, n, i):
            a[j] += num[i]
a[0] = k

# 부분합 구하는 공식을 이용해서 마무리한다.
for i in range(1, len(a)):
    a[i] += a[i - 1]
a = [0] + a

for _ in range(q):
    l, r = map(int, input().split())
    print(a[r+1] - a[l])