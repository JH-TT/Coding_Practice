mini, maxi = map(int, input().split())
eratos = [False] * (maxi - mini + 1)

res = maxi - mini + 1
for i in range(2, int(maxi ** 0.5) + 1):
    s = i ** 2
    for j in range((((mini-1) // s) + 1) * s, maxi+1, s):
        if not eratos[j - mini]:
            eratos[j - mini] = True
            res -= 1

print(res)

# 에라토스테네스의 체 문제
# 기존의 i * j로 따지지 않고 i * i 인 제곱으로 따졌다고 생각하면 됨.
# 그리고 시작지점도 다르기때문에 약간의 조정이 필요하다는 것도 필요함.