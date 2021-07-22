n = int(input())

arr = [[0] * 10 for _ in range(n + 1)]
m = 10**9

for i in range(1, 10):
    arr[1][i] = 1

for i in range(1, n):
    arr[i + 1][0] = arr[i][1]
    arr[i + 1][9] = arr[i][8]
    for j in range(1, 9):
        arr[i + 1][j] = arr[i][j - 1] + arr[i][j + 1] # 이전 자릿수의 값이j이면, 이보다 더 큰 자릿수의 j-1와 j+1의 값을 더해준다.
print(sum(arr[-1]) % m)

# 1자리는 모든 수가 계단 수.(line 6-7 참고)
# 2자리부터는 예를들면 일의자리가 3인걸 보면, 23, 43 이렇게 있다. 즉 십의자리인 2의값과 4의값을 더해서 3에다 저장하는 식이다. (line 13참고.)
# ex) 3자리 일의자리 3 -> #23, #43 이런식.