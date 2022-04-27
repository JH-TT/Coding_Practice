import sys
input = sys.stdin.readline

n, m, h = map(int, input().split())

info = [[1] + [0]*h for _ in range(n+1)] # 0은 무조건 만들기때문에 1로 시작.

for i in range(1, n+1):
    info[i] = info[i-1].copy() # 블럭을 하나도 놓지 않는경우엔 이전정보를 그대로 이어간다.
    a = list(map(int, input().split()))
    for j in a:
        for k in range(j, h+1):
            info[i][k] += info[i-1][k-j] # j높이의 블럭은 이전정보에서 k-j높이에서 j를 놓는것이기 때문에 k-j의 경우의 수를 그대로 더해준다.
print(info[n][h] % 10007)