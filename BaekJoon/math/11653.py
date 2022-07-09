n = int(input())

d = 2
while d <= n:
    if n % d == 0:
        print(d)
        n /= d
    else:
        d += 1

# d가 n을 넘지 않을때
# d가 n을 나누어 떨어지게 하면 출력후 n을 d로 나눈 몫을 이어서 감.
# 아니면 d값을 증가시킴.