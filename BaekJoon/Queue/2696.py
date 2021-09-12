# 내가 한 코드.
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    q, r = divmod(n, 10)
    num = []
    # 입력도 10개 단위로 주어지기 때문에 10으로 나눈 나머지를 기준으로 입력받는다.
    if r == 0:
        for _ in range(q):
            num.extend(list(map(int, input().split())))
    else:
        for _ in range(q + 1):
            num.extend(list(map(int, input().split())))
    
    # center1과 2를 만들어서 서로 번갈아가면서 요소를 입력받는다.
    center1 = []
    center2 = []
    heapq.heappush(center1, num.pop(0))
    print(n//2 + 1) # 총 중앙값 개수
    print(center1[0], end=" ")
    print_cnt = 1
    while num:
        if len(center1) > 0:
            # 2개씩 힙으로 옮긴다.
            for _ in range(2):
                heapq.heappush(center1, num.pop(0))
            # heappop을 이용해서 다른 리스트로 옮긴다.(정렬됨)
            while center1:
                center2.append(heapq.heappop(center1))
            # 그 중에 중앙값을 구하고 print_cnt를 1 증가시킨다..
            print(center2[len(center2) // 2], end=" ")
            print_cnt += 1
            if print_cnt == 10:
                print()
                print_cnt = 0
        else:
            for _ in range(2):
                heapq.heappush(center2, num.pop(0))
            while center2:
                center1.append(heapq.heappop(center2))
            print(center1[len(center1) // 2], end=" ")
            print_cnt += 1
            if print_cnt == 10:
                print()
                print_cnt = 0
    print()
#

# 더 빨리 실행되는 코드.
import heapq
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    q, r = divmod(int(input()), 10) # 입력받은 숫자를 10으로 나눠서 몫과 나머지를 반환한다.
    num = [] # 리스트 입력받을 곳
    # 나머지가 없으면 q만큼 입력받는다. 나머지가 있으면 q+1만큼 입력받는다.(입력을 10개 단위로 입력받음.)
    if r == 0:
        for _ in range(q):
            num.extend(list(map(int, input().split())))
    else:
        for _ in range(q + 1):
            num.extend(list(map(int, input().split())))
    
    r, l = [], []
    m = num[0]
    ans = [m]
    for i, v in enumerate(num[1:], 1):
        if v > m: # v값이 m보다 크면 r리스트에 넣음.
            heapq.heappush(r, v)
        else: # 작으면 l에 넣되 최대힙으로 넣음.(꺼낼때 m보다 작지만 가장 큰 값을 꺼내기 위해)
            heapq.heappush(l, -v)
        # 홀수번쨰마다 ans에 중앙값을 넣음.
        if i % 2 == 0:
            if len(r) > len(l): # r의 길이가 더 길다는 것은 m보다 큰 값들이 더 많다는것. 즉 m은 중앙값이 아니라는 것이다.
                heapq.heappush(l, -m) # 그러니 m을 l리스트에 넣고, r에서 heappop으로 꺼낸다.
                m = heapq.heappop(r)
            elif len(r) < len(l):
                heapq.heappush(r, m)
                m = -heapq.heappop(l)
            # 한 번만 실행하는 이유는 어차피 2개가 들어갈떄 마다 실행되기 때문에 한 번만 실행해도 r과 l의 길이는 같아지게 된다.
            ans.append(m)
    print(len(ans)) # 총 중앙값 개수
    # 10개씩 출력.
    i = 0
    for _ in range(len(ans) // 10):
        print(*ans[i:i+10])
        i += 10
    print(*ans[i:])