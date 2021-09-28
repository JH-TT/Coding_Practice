n = int(input())

seq = list(map(int, input().split()))
cnt = [1] * n
res = [[] for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i]:
            cnt[i] = max(cnt[i], cnt[j] + 1)

res = [0] * max(cnt) # res에 지정해서 넣기위함.
start = max(cnt) - 1 # 거꾸로 탐색하기때문에 끝 인덱스부터 시작.
max_index = cnt.index(max(cnt)) # 현재 자기보다 작은 수가 많은 위치 초기화.
max_cnt = max(cnt) # 그때의 값 초기화.
for i in range(max_index, -1, -1): # 거꾸로 탐색.
    if cnt[i] == max_cnt: # 만약 현재 위치의 개수가 max_cnt와 같으면
        res[start] = seq[i] # start위치에 값을 넣는다
        max_cnt -= 1 # 이때 max_cnt의 값을 1감소.
        start -= 1 # 다음에 넣을 인덱스지정.

print(len(res))
print(*res)

# 11053번 가장 긴 증가하는 부분 수열문제가 들어가고
# 거기에 탐색하는 부분만 추가된 문제.
# 각 입력된 숫자마다 그 숫자보다 왼쪽에 작은 수들의 개수를 구하고
# 가장 개수가 많은 인덱스부터 탐색한다.