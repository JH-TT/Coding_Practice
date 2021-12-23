import sys
input = sys.stdin.readline

n = int(input())
res = []
for _ in range(n):
    arr = list(map(int, input().split()))
    res += arr
    res.sort(reverse = True)
    res = res[:n]
print(res[-1])

# 입력받으면 정렬 후 상위 n개씩 계속 슬라이싱을 해주고 마지막 값을 출력한다.