import sys
input = sys.stdin.readline

def gcd(a, b):
    while True:
        r = a % b
        if r == 0:
            return b
        a = b
        b = r


for _ in range(int(input())):
    m, n, x, y = map(int, input().split())

    lcm = (m * n) / gcd(m, n)

    cnt = 0
    while True:
        left = m * cnt + x
        if left > lcm:
            print(-1)
            break
        if (left % n) == (y % n):
            print(left)
            break
        cnt += 1

# 최소공배수 문제
# 어떤 수 k에 대해서 M으로 나누었을때 나머지가x, N으로 나누었을때 y를 만족하는 k를 찾는 문제다.
# 이경우에는 한 쪽을 기준으로 오른쪽이 조건이 맞으면 값을 출력하는 방식으로 하면 된다.
# 없으면 -1을 뱉어야 하는데, 이건 최소공배수를 넘으면 -1을 뱉도록 하면 된다.