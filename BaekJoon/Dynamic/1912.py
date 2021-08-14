n = int(input())
z = list(map(int, input().split()))

for i in range(1, n):
    z[i] = max(z[i - 1] + z[i], z[i])
print(max(z))
# 인덱스 i의 값 + 인덱스 i - 1의 값 과 인덱스 i의 값중에 더 큰 값을 z[i]에 넣는다.
# 지금까지 더한값이랑, 다시 한 개의 수부터 시작하는 것중에 어떤것이 더 큰지 비교하는것.