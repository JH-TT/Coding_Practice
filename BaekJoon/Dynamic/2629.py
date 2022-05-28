n = int(input())
weights = list(map(int, input().split()))
n2 = int(input())
marbles = list(map(int, input().split()))
t_w = sum(weights)
ans = [[0 for _ in range(2*t_w+1)] for _ in range(n)] # 중앙이 무게 0, 왼쪽은 -, 오른쪽은 +
ans[0][t_w + weights[0]] = 1
ans[0][t_w - weights[0]] = 1

for i in range(1, n):
    ans[i] = ans[i-1].copy()
    ans[i][t_w + weights[i]] = 1
    ans[i][t_w - weights[i]] = 1
    for j in range(2*t_w+1):
        if ans[i-1][j] == 1:
            plus = j + weights[i]
            minus = j - weights[i]            
            ans[i][plus] = 1
            ans[i][minus] = 1
          
for i in marbles:
    if t_w < i:
        print("N", end=" ")
    else:
        print("Y" if ans[-1][t_w + i] == 1 else "N", end=" ")


# 추의 무게를 서로 더하고 뺄 수 있기떄문에, 총 추의 무게를 중심으로 리스트길이를 2배로 만듦.
# 그 외에는 냅색문제처럼 풀이.