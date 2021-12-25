import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    element = defaultdict(int) # defaultdict(int)를 해주면 value가 가본적으로 0이다. 즉 처음부터 연산이 가능.
    Min_Q = []
    Max_Q = []
    for _ in range(k):
        cmd, num = input().split()        
        if cmd == "I":
            heapq.heappush(Min_Q, int(num))
            heapq.heappush(Max_Q, -int(num))
            element[int(num)] += 1 # defaultdict(int)로 설정했기때문에 바로 연산 가능.(같은 숫자가 들어갈 수 있기 때문에 +1을 해준다.)
        else:            
            # 먼저 존재하지 않는 숫자들은 반복문으로 빼준다음, 현재 최댓값(최솟값)을 빼준다.
            if num == "1":              
                while Max_Q and not element[-Max_Q[0]]:
                    heapq.heappop(Max_Q)
                if Max_Q:
                    element[-Max_Q[0]] -= 1
                    heapq.heappop(Max_Q)
            else:
                while Min_Q and not element[Min_Q[0]]:
                    heapq.heappop(Min_Q)
                if Min_Q:
                    element[Min_Q[0]] -= 1
                    heapq.heappop(Min_Q)
    # 마지막으로 현재 존재하지않는데 힙 안에 아직 있을 수 있으니 한번 더 실행한다.
    while Max_Q and not element[-Max_Q[0]]:
            heapq.heappop(Max_Q)
    while Min_Q and not element[Min_Q[0]]:
            heapq.heappop(Min_Q)
    

    if Max_Q and Min_Q:
        print(-Max_Q[0], Min_Q[0])
    else:
        print("EMPTY")

# 이 문제는 생각하는데는 어렵지 않았는데, 같은 숫자가 들어간다는 것을 인지하지않고 해서 애먹은 문제.
# defaultdict(int)의 특징을 알게됨.        