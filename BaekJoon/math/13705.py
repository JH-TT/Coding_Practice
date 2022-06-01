import math
from decimal import *
getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP
# 부동 소수점 이용.
a, b, c = map(Decimal, map(int, input().split()))
pi = Decimal('3.14159265358979323846264338327950288419716939937510')

# 사인함수를 직접 구현한 코드.
def sin(x):
    if -pi <= x <= pi:
        getcontext().prec += 2
        i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
        while s != lasts:
            lasts = s
            i += 2
            fact *= i * (i-1)
            num *= x * x
            sign *= -1
            s += num / fact * sign
        getcontext().prec -= 2
        return +s
    elif x > pi:
        while x > pi:
            x-=2*pi
        return sin(x)
    elif x < -pi:
        while x < -pi:
            x+=2*pi
        return sin(x)

def f(x):
    return a*x + b*Decimal(sin(x)) - c

left = c / a - Decimal('1')
right = c / a + Decimal('1')
while right - left > Decimal(1e-20):
    mid = (left + right) / 2
    if f(mid) > 0:
        right = mid
    elif f(mid) < 0:
        left = mid
    else:
        break
print(round((left + right) / 2, 6))

# 정확한 계산을 위해 부동소수점 도입함.