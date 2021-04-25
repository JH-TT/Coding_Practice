# 방법1 경우의 수로 이용.
# 2와 1을 나열하는 경우의 수에다가, 2를 나열하는 경우의 수, 1을 나열하는 경우의 수를 각각 나눠준다.
# ex) 2 2 2 1 1 인 경우엔 5!/3!*2! 로 푸는것이다.
import math

n = int(input())

sum = 0
t = n // 2
for i in range(t + 1):
    sum += math.factorial(n - i) // (math.factorial(i) * math.factorial(n - i*2))
print(int(sum) % 10007)

# 방법2 피보나치 이용.
# n열의 타일링을 채우는 경우의 수를 f(n)이라고 했을 때, f(n)은 오른쪽 가장 끝에 가로블록 2개를 채운 경우 + 세로블록 1개를 채운 경우이기 때문에
# f(n) = f(n - 2) + f(n - 1) 이 된다.
n = int(input())

d = [0] * 1001
d[0] = 1
d[1] = 1

for i in range(2, n + 1):
    d[i] = d[i - 2] + d[i - 1]
print(d[n] % 10007)