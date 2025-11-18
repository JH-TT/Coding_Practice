def matmul(x, y):
  z = [[0] * 8 for _ in range(8)]
  for i in range(8):
      row_i = x[i] # x의 행
      zi = z[i] # 결과값의  행
      for j in range(8):
          if row_i[j] == 0:
              continue
          rij = row_i[j]
          yj = y[j]
          for h in range(8):
              zi[h] = (zi[h] + rij * yj[h]) % MOD
  return z

def matpow(M, n):
  result = [[1 if i == j else 0 for j in range(8)] for i in range(8)] # Identity 행렬
  base = M

  while n > 0:
      # 홀수인 경우, base를 result에 곱한다.
      if n & 1:
          result = matmul(result, base)
      base = matmul(base, base)
      n >>= 1

  return result

A = [[0] * 8 for _ in range(8)]
# 문제에 이미 그래프 형태가 주어졌음.
graph = [[1, 2], [0, 2, 3], [0, 1, 3, 4], [1, 2, 4, 5], [2, 3, 5, 6], [3, 4, 7], [4, 7], [5, 6]]
for i in range(8):
  for j in graph[i]:
      A[i][j] = 1

MOD = 1_000_000_007

n = int(input())

ANS = matpow(A, n)

# ANS[0][0]: 0번노드에서 시작해 0번노드로 끝나는 모든 경우의 수
print(ANS[0][0] % MOD)

# 행렬곱 분할정복문제
# A^n[i][j] -> i 에서 j까지 n분 지났을 때 모든 경우의 수가 된다.
# 왜 행렬곱이냐? 행렬곱을 풀어서보면 중간지점 k를 두고 i ~ j 까지 모든 경우의 수를 계산하는 모습이 된다.
# 따라서 행렬곱을 이용하면 된다.