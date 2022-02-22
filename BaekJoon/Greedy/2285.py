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