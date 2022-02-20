import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
box = [list(map(int, input().split())) for _ in range(m)]
truck = [0] * (n+1) # 현제 구간에서의 실은 택배
res = 0

box.sort(key=lambda x : (x[1], x[0])) # 도착도시 기준 정렬, 같으면 시작 도시 정렬
print(box)
for i in range(m):
    cnt = 0
    for j in range(box[i][0], box[i][1]):
        cnt = max(cnt, truck[j])
    left = min(box[i][2], c - cnt)
    res += left
    for j in range(box[i][0], box[i][1]):
        truck[j] += left
print(res)

# reference : https://jaimemin.tistory.com/764