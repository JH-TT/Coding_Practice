import heapq
import sys
input = sys.stdin.readline

# 힙 이용(걸린시간 6648ms)
T = int(input())
while T:
    n = int(input())
    a = []
    for _ in range(n):
        heapq.heappush(a, list(map(int, input().split())))
    print(a)
    x, y = heapq.heappop(a)
    b = y
    cnt = 1
    for _ in range(1, n):
        if b > a[0][1]:
            b = a[0][1]
            cnt += 1
            if b == 1:
                break
        heapq.heappop(a)
    print(cnt)
    T -= 1

# 리스트 이용(걸린시간 5896ms)
T = int(input())
while T:
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort()
    b = a[0][1]
    cnt = 1
    for i in range(n - 1):
        if b > a[i + 1][1]:
            b = a[i + 1][1]
            cnt += 1
            if b == 1:
                break
    print(cnt)
    T -= 1
# 힙이 더 느리다 아마 힙은 pop이나 push의 시간 복잡도가 O(logn)이고, 즉 총 O(nlogn)이 걸림.
# 리스트 이용한 부분은 sort만 있었기 떄문에 O(nlogn) 그 외에 for문 부분은 모든 계산의 시간복잡도가 O(1)걸림 총O(n).
# 어떻게 보면 둘이 비슷한거 같은데 리스트부분이 더 빠른 이유는 아마도 아래코드는 리스트컴프리헨션을 이용해서 그런거 같다.