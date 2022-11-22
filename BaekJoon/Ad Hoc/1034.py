n, m = map(int, input().split())

chotbul = []
for _ in range(n):
    chotbul.append(input())

k = int(input())
res = 0
for i in range(n):
    zero_cnt = chotbul[i].count("0")
    col_cnt = 0
    if zero_cnt <= k and zero_cnt % 2 == k % 2:
        for j in range(n):
            if chotbul[i] == chotbul[j]:
                col_cnt += 1
    res = max(res, col_cnt)
print(res)

# 각 행마다 0의 개수를 구한다.
# 모든 양초가 켜질 조건
# 1. 0의 개수가 k보다 작거나 같다.
# 2. 0이 짝수면 k도 짝수, 0이 홀수면 k도 홀수여야 한다.
# 이걸 먼저 구하고 그 행과 같은 모양이 몇개있는지 확인한다.
# 그 중에 가장 많은 개수를 출력한다.

# 느낀점....
# 이 문제는 작은단위(각 행)에서 큰 단위로 가는 단계였다.
# 나는 전체를 보고 한번에 풀려고해서 잘 안됐다.