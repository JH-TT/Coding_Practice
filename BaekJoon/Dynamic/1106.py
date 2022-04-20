import sys
input = sys.stdin.readline

INF = 10**6

c, n = map(int, input().split())
customer = [0] + [INF for _ in range(c)]

for _ in range(n):
    cost, cust = map(int, input().split())
    for i in range(1, c+1):
        if i >= cust:
            customer[i] = min(customer[i], customer[i-cust] + cost)
        else:
            customer[i] = min(customer[i], cost)
print(customer[-1])          

# 풀이
# 두가지로 나뉜다.
# 1. 현재 i명일때 그 i명이 cust보다 적을때
# 2.          "                  클때

# 1.이면 i가 cust이상이 될 때 까지 cost와 현재값이랑 비교해서 더 작은값으로 업데이트한다.
# 2.면 현재값이랑 i-cust명의 비용 에서 cost를 더한값 중에 비교해서 업데이트한다.
# customer리스트의 마지막을 출력한다