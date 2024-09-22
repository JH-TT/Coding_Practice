import sys
input = sys.stdin.readline

n = int(input())
h = []
total = 0
for _ in range(n):
    a, b = map(int, input().split())
    h.append([a, b])
    total += b
h.sort()    

people = 0
for a, b in h:
    people += b
    if people > total//2:
        print(a)
        break

# 이 문제의 핵심
# 가장 앞에있는 집부터 사람 수를 더하다가 전체 사람수 절반보다 커지는 시점이 최소가 되는 위치이다.

# 반례등장 2024-09-22
# 4
# 10 1
# 20 3
# 25 2
# 40 2
# 정답 : 20
# 해당 코드 답 : 25
# 따라서 위에 절반이 넘을때 값으로 할 수 없다.
# 그래서 직접 각 노드별 거리 총합을 비교해서 가장 작을때 위치를 출력하는 방식으로 변경

import sys
input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    a, b = map(int, input().split())
    h.append([a, b])
h.sort()

prefix_sum = [0]
left = 0
right = 0
for i in range(n):
    prefix_sum.append(prefix_sum[-1] + h[i][1])
    right += abs(h[0][0] - h[i][0]) * h[i][1]

res = right
res_pos = h[0][0]
for i in range(1, n):
    d = h[i][0] - h[i-1][0]
    left += d * prefix_sum[i] # 오른쪽으로 우체국이 이동하면 우체국 왼쪽의 거리 총합 변화
    right -= d * (prefix_sum[-1] - prefix_sum[i]) # 우체국 오른쪽의 거리 총합 변화
    if left + right < res:
        res = left + right
        res_pos = h[i][0]
print(res_pos)
# 가장 왼쪽에 우체국이 위치할때 시작으로 오른쪽 으로 이동할 때 마다 값이 어떻게 변하는지 규칙을 찾아서 총 거리 합을 빠르게 도출해서 진행