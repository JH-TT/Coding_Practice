import sys
import heapq # 힙을 이용해 우선순위 큐를 만들것(heapq가 priorityqueue보다 빠름)
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)] # 각 수업 시간을 입력받음.
arr = sorted(a) # 오름차순으로 정렬

queue = list() # 빈 리스트 생성.
heapq.heappush(queue, arr[0][1]) # 큐에 첫수업 끝나는 시간을 입력

for c in arr[1:]: # 2번째꺼 부터 비교
    if c[0] >= queue[0]: # 수업시작시간 >= 전 수업 끝나는 시간이면 같은 강의실에서 수업들을 수 있다.
        heapq.heappop(queue) # 원래있던 끝나는시간을 그 다음 수업 끝나는 시간으로 변경 pop하고 push한다.
    heapq.heappush(queue, c[1])
print(len(queue)) # 큐의 길이가 강의실의 개수.