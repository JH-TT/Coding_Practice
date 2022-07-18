a, b = input().split()

d = len(b) - len(a)
res = 100
for i in range(d+1):
    s_res = 0
    for j in range(len(a)):
        if b[j+i] != a[j]:
            s_res += 1
    res = min(res, s_res)
print(res)

# 더 짧은 문자열을 한 칸씩 오른쪽으로 옮기면서 긴 문자열과 각 위치마다 비교한다.
# 짧은 문자열 돌 때마다 res 업데이트 해준다.