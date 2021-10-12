n = int(input())

candy = [list(input()) for _ in range(n)]

def check(a):
    cnt = []
    # 행 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if a[i][j-1] == a[i][j]:
                count += 1
            else:
                cnt.append(count)
        cnt.append(count)

    # 열 검사
    for i in range(n):
        count = 1
        for j in range(1, n):
            if a[j-1][i] == a[j][i]:
                count += 1
            else:
                cnt.append(count)
        cnt.append(count)
    
    return max(cnt)

result = check(candy)
if result == n:
    print(result)
    exit(0)

# 행 교환
for i in range(n):
    for j in range(1, n):
        if candy[i][j - 1] != candy[i][j]:
            candy[i][j - 1], candy[i][j] = candy[i][j], candy[i][j - 1]
            result = max(result, check(candy))
            candy[i][j - 1], candy[i][j] = candy[i][j], candy[i][j - 1]

# 열 교환
for i in range(n):
    for j in range(1, n):
        if candy[j - 1][i] != candy[j][i]:
            candy[j - 1][i], candy[j][i] = candy[j][i], candy[j - 1][i]
            result = max(result, check(candy))
            candy[j - 1][i], candy[j][i] = candy[j][i], candy[j - 1][i]

print(result)

# 일반적인 부루스포스 알고리즘.
# 사탕을 교환하면 check함수를 돌려 가장 킨 문자열을 체크.

# 이것보다 빠르게 하려면 바뀐 부분에 대한 행과 열만 체크하면됨. 나는 바뀐부분 관계없이 전부 확인해서 좀 걸렸다.