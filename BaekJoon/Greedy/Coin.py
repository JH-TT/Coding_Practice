a, b = map(int, input().split())
result = 0  # 동전의 개수
m = []  # 동전의 가치
for i in range(a):
  m.append(int(input()))
for j in m[::-1]: # 큰 것부터 봐야하니 역으로 빼낸다.
    result += b // j  # 몫이 개수이므로 몫을 result에 넣음
    b %= j  # 남은 돈
print(result)