import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

result = [0] + (n + 1)

M = 0
for i in range(n):
    M = max(M, result[i]) # 현재시점에서 수익
    if i + s[i][0] <= n:
        result[i+s[i][0]] = max(M + s[i][1], result[i+s[i][0]]) # max(가장 많은 수익 + 이번 상담 수익, 이번 상담이 끝날때 수익) 중 큰걸로 업데이트.
    
print(max(result))

# 참고 : https://dndi117.tistory.com/entry/aaa