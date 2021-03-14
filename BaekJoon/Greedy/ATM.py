ATM기 문제
import sys
input = sys.stdin.readline
n = int(input()) # 몇명인지
p = list(map(int, input().split())) # 각 사람마다 걸리는 시간
p.sort() # 오름차순으로 정렬해야 최솟값 나옴
t = [] # 각 사람마다 총 걸리는 시간
for i in range(n):
    t.append(sum(p[:i + 1])) # i번째 사람이 걸리는 총 시간은 i번째 까지 각각 걸리는 시간의 합.
print(sum(t))