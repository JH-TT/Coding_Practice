n = int(input())
wine = [int(input()) for _ in range(n)]

# ans의 i번째 인덱스라는 의미는, i번째 와인을 마신다는 가정하에 최댓값을 저장하는 공간이다.
ans = [0] * n
ans[0] = wine[0]
if n > 1:
    ans[1] = wine[0] + wine[1]
if n > 2:
    ans[2] = wine[2] + max(wine[0], wine[1])
if n > 3:
    ans[3] = wine[3] + max(wine[2] + ans[0], ans[1])

# 4번째 와인부터는 
# 1) 2번째 와인을 마신다는 가정하에 최댓값 
# 2) 1번째 와인을 마신다는 가정하에 최댓값 + 3번째 와인
# 3) 0번째 와인을 마신다는 가정하에 최댓값 + 3번째 와인 중에 최댓값을 지정한다.
for i in range(4, n):
    ans[i] = wine[i] + max(ans[i - 2], ans[i - 3] + wine[i - 1], ans[i - 4] + wine[i - 1])
print(max(ans))
# 2579(계단 오르기와 비슷함)