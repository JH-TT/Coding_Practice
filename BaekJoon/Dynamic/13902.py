from itertools import combinations

n, m = map(int, input().split())
w = list(map(int, input().split()))
w2 = combinations(w, 2)

# 전처리.
for i in w2:
    if i[0] + i[1] <= n: # 두 손을 이용했을 때 짜장면 개수가 n개 이하인 경우만 넣는다.
        w.append(i[0] + i[1])
w = list(set(w)) # 중복 제거.

zzazang = [20000] * (n + 1)
zzazang[0] = 0

for i in w:
    for j in range(i, n + 1):
        # 최솟값부터 현재 j개의 짜장면의 최솟값, j - i 개의 짜장면 최솟값 + 1 중에서 더 작은 값을 j개의 짜장면 최솟값으로 설정한다.
        zzazang[j] = min(zzazang[j], zzazang[j - i] + 1)

print(zzazang[n] if zzazang[n] != 20000 else -1) # 만들 수 있으면 그 값을 출력하고, 아니면 -1을 출력한다.