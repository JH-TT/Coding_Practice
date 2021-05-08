import sys # 빠르게 입력받기
import heapq # 힙을 이용해서 풀기
input = sys.stdin.readline

n = int(input())
card = []
result = 0
for _ in range(n):
    heapq.heappush(card, int(input()))
while len(card) > 1:
    x = heapq.heappop(card); y = heapq.heappop(card) # 앞에 2개를 pop한 뒤에
    result += x + y # result에 x + y를 더해놓고
    heapq.heappush(card, x + y) # x + y를 다시 push한다.

print(result)

# 이 문제 핵심은 오름차순으로 정렬하고, 이때 작은 두 수 부터 시작해서 올라가는 형식이다.
# 이럴때 유용한 것이 바로 힙이다. 뽑을때 알아서 최솟값이 빠지게 돼 있기 때문이다.