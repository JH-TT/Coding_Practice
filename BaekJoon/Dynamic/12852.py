# 내가 짠 코드

n = int(input())
INF = float('inf') # 최댓값
dp = [INF] * (n + 1)
arr =  [[] for _ in range(n+1)]
dp[1] = 0
arr[1] = [1]
# 보텀업 방식 이용.
# dp값이 갱신 될 때마다 arr을 지금까지 트랙 + 현재 위치로 갱신한다
for i in range(2, n+1):
    if dp[i-1] + 1 < dp[i]:
        dp[i] = dp[i-1] + 1
        arr[i] = [i] + arr[i-1]
    if i % 2 == 0:
        if dp[i//2]+1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            arr[i] = [i] + arr[i // 2]
    if i % 3 == 0:
        if dp[i//3]+1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            arr[i] = [i] + arr[i // 3]     
print(dp[n])
print(*arr[n])

# 다른 고수분의 코드 훨씬 빠르고 메모리도 적게 들었음.
n = int(input())
dp = [-1 for _ in range (n+1)]
dp[1] = 0

def f(n):
    if n == 2:
        return 1
    if n == 3:
        return 1
    if dp[n] != -1:
        return dp[n]
    # 이 부분이 처음에 볼 때 이해가 안됐는데
    # 그냥 쉽게 생각하면 2, 3배 증가 후 1을 몇 번 증가시키는 경우라고 보면 됨.
    # f(n//2) -> 2배시킴
    # n % 2 -> 1을 몇 번 증가시킬지
    # ex) 9 -> 4에서 2배시키고 1증가
    #     9 -> 3에서 3배시키고 0증가 중에 최솟값 + 1이다.
    # 결국 (n//2까지 오는 경우의 수 + 2배 증가 + n까지 1씩 증가, n//3까지 오는 경우의 수 + 3배 증가 + n까지 1씩 증가)중에 최솟값을 dp값으로 두겠다는 것임.
    dp[n] = min(f(n//2)+n%2, f(n//3)+n%3)+1
    return dp[n]

print(f(n))

# 반복문 돌면서 1증가, 2배, 3배중에 더 적은 횟수로 오는경우를 ans에 넣어준다.
# 출력.
ans = [n]
while n > 1:
    app = n-1
    m = f(n-1)
    if n%2 == 0:
        if m > f(n//2):
            m = f(n//2)
            app = n//2
    if n%3 == 0:
        if m > f(n//3):
            m = f(n//3)
            app = n//3
    ans.append(app)
    n = app
for i in ans:
    print(i, end=" ")