# 1. 단순 투포인터로 구현
import math

n = int(input())
res = 0
# 에라토스테네스의 체로 소수 구해놓음
array = [True for _ in range(n+1)]
p = []
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:        
        j = 2
        while i*j <= n:
            array[i*j] = False
            j += 1
for i in range(2, n+1):
    if array[i]:
        p.append(i)

# 투 포인터 시작.
sum = 0
end = 0
for start in range(len(p)):
    while sum < n and end < len(p):
        sum += p[end]
        end += 1
    if sum == n:
        res += 1
    sum -= p[start]
print(res)  

# 2. 구간합(prefix sum) 이용
def get_prime(n) -> list:
  array = [True for _ in range(n+1)]
  p = []
  for i in range(2, int(n ** 0.5) + 1):
      if array[i]:
          j = 2
          while i*j <= n:
              array[i*j] = False
              j += 1
  for i in range(2, n+1):
      if array[i]:
          p.append(i)
  return p
    
def get_prefix(p) -> list:
    psum = [0]
    for prime in p:
        psum.append(psum[-1] + prime)

    return psum

n = int(input())
p_nums = get_prime(n)
psum = get_prefix(p_nums)

if len(psum) < 2:
    print(0)
else:
    cnt = 0
    s, e = 0, 1
    while s < e and e < len(psum):
        sum = psum[e] - psum[s]
        if sum == n:
            cnt += 1
            s += 1
            e += 1
        elif sum < n:
            e += 1
        else:
            s += 1
    print(cnt)

# 단순 투포인터 + 에라토스테네스의 체 이용하는 문제