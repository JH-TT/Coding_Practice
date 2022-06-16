import sys
sys.setrecursionlimit(10**6)

def dfs(n, a, b, num):
    k = 2**(n-1)
    h = k * k
    # 주어진 좌표가 현재 구역에 있는지 확인
    if r < a or r > a+2**n or c < b or c > b+2**n:
        return
    if a == r and b == c:
        print(num)
        exit()    
    if n == 0:
        return
    dfs(n-1, a, b, num)
    dfs(n-1, a, b+k, num+h)
    dfs(n-1, a+k, b, num+2*h)
    dfs(n-1, a+k, b+k, num+3*h)

N, r, c = map(int, input().split())
dfs(N, 0, 0, 0)

# 2**n * 2**n 배열을 4구역으로 나눈다.
# 주어진 좌표가 있는 구역을 제외한 나머지 3구역은 확인하지 않고 한 구역을 이어서 재귀돌린다.
# 맞는 좌표가 나올때 까지 돌린다.

# 오랜만에 재귀를 풀려고하니 꽤나 헷갈리네... 기본 dfs에 구역 확인하는 조건문 추가느낌