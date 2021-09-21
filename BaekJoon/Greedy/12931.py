n = int(input())

num = list(map(int, input().split()))

plus_cnt = 0
div_max = 0

for i in num:
    div = 0
    while i > 0:
        if i % 2 == 0:
            i //= 2
            div += 1
        else:
            i -= 1
            plus_cnt += 1
    div_max = max(div_max, div)
print(plus_cnt + div_max)

# 이 문제의 핵심
# 1을 더하는건 따로고 2를 곱하는것은 전부 곱해준다.
# 그러니 각 값들에 대해 0으로 만들떄 사용된 더하기 개수와 곱하기 개수를 구한다.
# 더하기는 각각 따로이므로 전부 더해주고, 곱하기는 전부 곱하는것이기 떄문에 그 중에 최댓값을 지정한다
# 마지막에 이 둘을 더해서 출력한다.