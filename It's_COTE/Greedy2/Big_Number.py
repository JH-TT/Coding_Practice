# 큰 수의 법칙
n, m, k = map(int, input().split())

a = list(map(int, input().split()))  # 입력받은 수들을 리스트로 저장
result = 0
max1 = max(a)  # 가장 큰 수
a.remove(max1)  # 가장 큰 수를 리스트에서 뺀다.
max2 = str(max(a)) # 이때 가장 큰 수는 2번째로 큰 수.
count = 0  # 연속으로 더한 횟수

for _ in range(m):
    if count == k:  # 가장 큰 수를 k번만큼 더했으면 다음은 2번째로 큰 수를 한 번 더한다.
        result += int(max2)
        count = 0
    else:
        result += max1
        count += 1
print(result)


# 문제집 답.

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()  # 입력받은 수들 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 k번 더하기
        if m == 0: # m이 0이면 반복문 탈출
            break 
        result += first
        m -= 1
    if m == 0:
        break
    result += second # 두 번쨰로 큰 수 한 번 더하기
    m -= 1
print(result)

# 그런데 이런식으로 하면 m이 엄청 큰 수일땐, 시간초과가 된다. 한 번 이렇게 생각 해 보자. 예시를 보면 가장 큰 수가6이고 다음이 5이고, k는 3이다. 이를 두번째 숫자를 더하는 순간까지 보면, 6 + 6 + 6 + 5 이고 이것이 반복됨을 알 수 있다. 길이는 이때 (k + 1)이고, m을 (k + 1)로 나눈 몫이 수열이 반복되는 횟수가 된다. 다시 K를 곱해주면 가장 큰 수가 등장하는 횟수인 것이다. 나누어 떨어지지 않을땐, 나머지만큼 가장 큰 수가 추가로 더해지므로 이를 고려해주어야 한다. 즉, 가장 큰 수가 더해지는 횟수는 int(m / (k + 1)) * k + m % (k + 1) 이다. 이를 토대로 다시 코드를 짜보면,

n, k, m = map(int, input().split())

data = list(map(int, input(),split()))
data.sort()

first = data[n - 1]
second = data[n - 2]
# 가장 큰 수가 더해지는 횟수
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first # 가장 큰 수 더하기
result += (m - count) * second # 두번째로 큰 수 더하기(m번 더하는데 거기서 count를 빼면 두번째로 큰 수를 더한 횟수가 된다.))
print(result)