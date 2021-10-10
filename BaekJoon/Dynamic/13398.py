n = int(input())

arr = list(map(int, input().split()))
m_value = [[0, 0] for _ in range(n)]

m_value[0] = [arr[0], 0] # 두 가지 경우(자신을 넣는 경우, 자신을 빼는 경우)
result = 0

for i in range(1, n):
    m_value[i][0] = max(m_value[i-1]) + arr[i]
    m_value[i][1] = max(0, m_value[i-1][1] + arr[i-1]) # 이전의 합들이 음수면 필요없으므로 0으로 초기화.
    result = max(result, max(m_value[i]))

if result == 0: # result가 0이라는 소리는 음수로만 이뤄져 있다는 의미.
    result += max(arr) # 음수중에 가장 큰 값을 더해준다.

print(result)