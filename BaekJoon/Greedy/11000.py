import heapq

n = int(input())

c = [list(map(int, input().split())) for _ in range(n)]

c.sort(key = lambda x : (x[0], x[1])) # 첫번째 인덱스로 정렬하고 같은값이면 두번째 인덱스로 정렬.

q = list()
heapq.heappush(q, c[0][1]) # 힙 이용.(디폴트 최소힙)

for i in c[1:]:
    if i[0] >= q[0]:
        heapq.heappop(q) # 최소힙이 디폴트라 pop을하면 최솟값이 빠져나옴.
    heapq.heappush(q, i[1])
print(len(q))
# 최소힙으로 된다는 것을 간과함.
# 풀이 방식은 쉽게 말하면 겹치는 시간(즉 수업끝나고 들을 수 있는 다음수업)끼리 하나로 압축하는 방식이라 생각하면 됨.
# ex) 1 3, 3 5 이렇게 있으면 1 5 이런식으로 압축.