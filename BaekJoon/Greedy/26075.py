n, m = map(int, input().split())
s = input()
t = input()

if n <= m:
    target = '0'
else:
    target = '1'

s_idx = [i for i in range(n + m) if s[i] == target]
t_idx = [i for i in range(n + m) if t[i] == target]
S = 0
T = 0
for i in range(min(n, m)):
    a = s_idx[i]
    b = t_idx[i]
    min_ = min(a, b)
    max_ = max(a, b)
    S += (max_ - min_) // 2
    T += (max_ - min_) // 2
    if (max_ + min_) % 2 != 0:
        if S <= T:
            S += 1
        else:
            T += 1
print(S**2 + T**2)

# 21 line 조건 필수!
# 만약 101 110 같은 둘 중에 한 명만 한 번 이동하면 되는 상황에서는 둘 중에 덜 움직인 사람이 움직이도록 한다!