n = int(input())
b = list(map(int, input().split()))
INF = float('inf')

res = []
for i in range(n):
    ans = 0
    left_t = INF
    right_t = -INF
    for j in range(i-1, -1, -1):
        nleft_t = float((b[i] - b[j])/(i - j))
        if nleft_t < left_t:
            left_t = nleft_t
            ans += 1
    
    for j in range(i + 1, n):
        nright_t = float((b[j] - b[i])/(j - i))
        if right_t < nright_t:
            right_t = nright_t
            ans += 1
    res.append(ans)
print(max(res))

# 이 문제는 기울기를 이용한다.
# 왼쪽을 탐색할땐, 기울기가 이전에 측정한 기울기보다 작아야 빌딩을 볼 수 있다.
# 오른쪽을 탐색할떈, 기울기가 이전에 측정한 기울기보다 커야 빌딩을 볼 수 있다.