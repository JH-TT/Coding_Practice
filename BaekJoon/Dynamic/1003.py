T = int(input())

for _ in range(T):
    n = int(input())
    fib = [[0, 0] for _ in range(41)]
    fib[0] = [1, 0]
    fib[1] = [0, 1]
    for i in range(2, n + 1):
        fib[i][0] = fib[i - 1][0] + fib[i - 2][0]
        fib[i][1] = fib[i - 1][1] + fib[i - 2][1]
    print(*fib[n])

# 그냥 피보나치를 메모이제이션을 이용하는것.
# 피보나치 값이 0과 1이 총 몇번 호출 되었는지와 같음.
# 그러니 0이 호출된 개수, 1이 호출된 개수를 나눠서 피보나치를 계산.