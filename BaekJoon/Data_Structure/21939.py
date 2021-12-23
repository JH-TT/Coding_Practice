import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())

problem_d = [] # 어려운거
problem_e = [] # 쉬운거
not_solve = defaultdict(bool) # 풀었는지 여부

for _ in range(n):
    p, l = map(int, input().split())
    heapq.heappush(problem_d, [-l, -p])
    heapq.heappush(problem_e, [l, p])
    not_solve[p] = True

m = int(input())

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "add":
        p = int(cmd[1])
        l = int(cmd[2])
        # 같은 번호의 다른 난이도 문제가 삽입되어 이미 죽은 문제인데 True로 나와 출력되는 것을 방지
        while not not_solve[-problem_d[0][1]]:
            heapq.heappop(problem_d)
        while not not_solve[problem_e[0][1]]:
            heapq.heappop(problem_e)
        not_solve[p] = True
        heapq.heappush(problem_d, [-l, -p])
        heapq.heappush(problem_e, [l, p])
    elif cmd[0] == "recommend":
        if cmd[1] == "1":
            while not not_solve[-problem_d[0][1]]:
                heapq.heappop(problem_d)
            print(-problem_d[0][1])
        else:
            while not not_solve[problem_e[0][1]]:
                heapq.heappop(problem_e)
            print(problem_e[0][1])
    else:
        not_solve[int(cmd[1])] = False

# 다른 풀이

import sys
import heapq
input = sys.stdin.readline
 
def recommend(flag,heap):
    flag = -flag
    while heap and (heap[0][1]*flag not in problem_dict.keys() or problem_dict[heap[0][1]*flag] != heap[0][0]*flag):
        heapq.heappop(heap)
    result = heap[0]
    result = result[1]*flag
    return result
 
N = int(input())
max_heap = []
min_heap = []
problem_dict = {}
for _ in range(N):
    pb_num,l_num = map(int,input().split())
    max_heap.append((-l_num,-pb_num))
    min_heap.append((l_num,pb_num))
 
    problem_dict[pb_num] = l_num
heapq.heapify(max_heap)
heapq.heapify(min_heap)
M = int(input())
 
for _ in range(M):
    command,*arg = input().split()
    if command == 'add':
        pb_num,l_num = map(int,arg)
        heapq.heappush(max_heap,(-l_num,-pb_num))
        heapq.heappush(min_heap,(l_num,pb_num))
        problem_dict[pb_num] = l_num
    elif command == 'solved':
        pb_num = int(arg[0])
        del problem_dict[pb_num]
    else:
        flag = int(arg[0])
        if flag > 0:
            print(recommend(flag,max_heap))
        else:
            print(recommend(flag,min_heap))