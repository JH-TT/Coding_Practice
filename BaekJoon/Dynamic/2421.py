# 에라토스테네스체를 이용해 미리 소수를 다 구해놓는다.
a = 1000 ** 2
eratos = [True] * (a + 1)
for i in range(2, int(a ** 0.5) + 1):
    if eratos[i]:
        j = 2
        while i * j <= a:
            eratos[i*j] = False
            j += 1

n = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]

# 로직 : 만약 ij로 이어진 숫자가 되는 경우는 (i-1)j 또는 i(j-1)에서 오는 경우뿐이다.
# 이 경우를 생각해 보면, ij가 만약 소수라면 (i-1)j, i(j-1) 중에서 큰 값에 1을 더한게 ij까지 소수의 개수가 되는것이다.
# 이를 코드로 옮기면 다음과같다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 and j == 1:
            continue
        arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        if eratos[int(str(i)+str(j))]:
            arr[i][j] += 1
print(arr[n][n]) # O(n^2) 이므로 n이 999이하여서 100만정도이다.(에라토스까지하면 대략 2n^2 정로도 생각하면 될듯하다.)