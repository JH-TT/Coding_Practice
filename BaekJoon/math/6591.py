import sys
input = sys.stdin.readline

def fac(n, k):
    up = 1
    down = 1
    for i in range(k):
        up *= (n-i)
        down *= (i+1)
      
    return up // down

while 1:
    n, r = map(int, input().split())
    r = min(r, n-r)
    if n == 0 and r == 0:
        break
    print(fac(n, r))

# 너무 라이브러리에 의존해서 풀었다.
# 이 문제는 combination을 더욱 쉽게 풀어서 써야한다. 