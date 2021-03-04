# 1이 될 때까지

# 내가 쓴 답
n, k = map(int, input().split())

count = 0  # 수행 횟수

while n != 1: # n이 1이면 종료
    if n % k == 0: # k로 나눠지면 k로 나눔
        n /= k
    else: # 나눠지지 않으면 1을 뺌
        n -= 1
    count += 1
print(count)
# 이렇게 해도 되지만, n이 엄청 커지면 이 풀이는 답이 안된다.

# 책(내가 한 거랑 조금 비슷)
n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k로 계속 나누기
while n >= k:
    # n이 k로 나누어 떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # k로 나누기
    n //= k
    result += 1
# while문을 빠져나오면 n은 k보다 작은 수. 즉 1이 될때까지 1씩 뺀다.
while n != 1:
    n -= 1
    result += 1

print(result)
# 이 방법도 n이 엄청 크면 해결이 안되므로, 좀 더 효율적으로 한 번에 빼는 방식으로 코드를 작성할 수 있다.
n, k = map(int, input().split())
result = 0

while True:
    # (n == k로 나누어떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)