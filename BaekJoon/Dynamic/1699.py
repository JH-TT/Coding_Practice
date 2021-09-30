import math

n = int(input())

cnt = [100001] * 100001

for i in range(1, int(math.sqrt(100000)) + 1):
    cnt[i*i] = 1

for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        cnt[i] = min(cnt[i], cnt[i - j*j] + 1) # 가능한 제곱으로 해서 뺴준다. -> 제곱은 항이 1개만 나오므로 최솟값으로 만들 수 있음.

print(cnt[n])