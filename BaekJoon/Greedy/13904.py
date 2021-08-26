n = int(input())
study = []
res = [0 for _ in range(1000)]

for i in range(n):
    d, w = map(int, input().split())
    study.append([d, w])
study.sort(reverse = True, key = lambda x : x[1]) # 역순으로 정렬.

for i in range(n):
    for j in range(study[i][0] - 1, -1, -1):
        if res[j] == 0: # 마감 날짜부터 반대로 돌면서 점수가 매겨지지않은 날짜에 그 값을 넣는다.
            res[j] = study[i][1]
            break
print(sum(res))

# 내가 한 방식
import sys
input = sys.stdin.readline

n = int(input())
study = [[] for _ in range(1001)] # 최대 마감일이 1000일까지 
index = [] # 마감일 저장할 곳.

for _ in range(n):
    d, w = map(int, input().split())
    index.append(d)
    study[d].append(w)

index.sort() # 마감날짜순으로 정렬.
index = set(index) # 중복 날짜 제거.
res = []
for i in index:
    study[i].sort(reverse = True) # 과제점수를 내림차순으로 정렬.
    if len(study[i]) > 1:
        for j in range(i):
            if j == len(study[i]): # 만약 과제개수가 마감날짜보다 적으면 종료.
                break
            res.append(study[i][j])
        res.sort(reverse = True) # 내림차순 정렬.
        res = res[:i] # 마감날짜만큼 슬라이싱.(i일까지의 최대값)
    elif len(study[i]) == 1: # 1개면 그냥 res에 넣음.
        res.append(study[i][0])

print(sum(res)) # 총합