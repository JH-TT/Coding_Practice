def solution(n, count):
  answer = 0
  dp = [[0 for _ in range(i+1)] for i in range(101)]
  # dp[a][b] -> a개로 b개의 층으로 구분되도록 놓는 경우의 수. 이때 b <= a
  # n개로 n층을 만들려면 결국 오름차순이 답임. 11 22 33 이런식으로 밖에 안나옴 왜냐하면 작은 블럭 사이에 큰 블럭이 들어갈 수 없기 때문 -> 1가지 뿐
  dp[0][0] = 1 # sum(dp[0])이 1이 나오도록 하기 위함
  dp[1][1] = 1

  dp[2][1] = 2
  dp[2][2] = 1

  for i in range(3, 101):
      # 1칸
      # j: k블럭 사이에 있는 블럭 개수
      for j in range(i):
          dp[i][1] += (C(i-1, j) * sum(dp[j]) * sum(dp[i-1-j]))
      dp[i][1] %= 1000000007
      # 2칸 ~ i-1칸
      # (k블럭 제외 왼쪽 블럭 구분 j-1높이 경우의 수) + (k블럭 포함 오른쪽 블럭 구분 높이 1 경우의 수) 가 점화식이 된다.
      for j in range(2, i):
          # k블럭기준 왼쪽자리 개수 (가장 큰 블럭을 제외하면 최소 서로다른크기의 블럭 j-1개가 왼쪽에 있어야 한다)
          for h in range(j-1, i):
              dp[i][j] += (C(i-1, h) * dp[h][j-1] * dp[i-h][1])
          dp[i][j] %= 1000000007
      # i칸
      dp[i][i] = 1

  return dp[n][count]

def C(k, n):
  if n == 0 or n == k: return 1
  if n == 1 or n == k - 1: return k
  son = 1
  pa = 1
  for i in range(n):
      son *= (k - i)
      pa *= (n - i)
  return son // pa

# 10억7을 나누는 타이밍을 잘못잡아서 1시간동안 삽질함...
# 단순 덧셈이 아닌, 곱셈을 한 뒤에 합치는 경우는 전부 합친 다음에 나누도록 한다.