import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
h = [0] * 257 # 각 높이의 개수

for i in range(n):
    for j in range(m):
        h[arr[i][j]] += 1 # arr[i][j]높이의 개수를 1개씩 늘린다.
      
INF = 10**10        
ans = [INF, 0] # [시간, 높이]
for i in range(257):
    t = 0 # 시간
    k = 0 # 들어가고 나오는 블럭 개수. 양수면 들어간것 음수면 뺴온것
    for j in range(257):
        # j높이의 블럭을 i높이까지 뺌.
        if j > i:
            t += h[j] * 2 * (j - i) # 캐는데 시간이 2가 걸린다 했음.
            k += h[j] * (j - i) # 인벤토리에 블럭이 추가됨.
        # j높이의 블럭을 i높이까지 추가함.
        elif j < i:
            t += h[j] * (i - j) # 추가하는데는 시간이 1이 걸림.
            k -= h[j] * (i - j) # 인벤토리에서 빼옴.
    if k + b < 0: # 인벤토리에 있는 블럭개수보다 많이 쓰면 만들 수 없는 높이.
        break # 그 이상의 높이도 만들 수 없기에 반복문을 빠져나옴.
    if t <= ans[0]: # 시간이 더 적게 걸리거나 같으면
        ans = [t, i] # 현재 정보로 바꿈. 시간이 같으면 더 높은 높이로 출력해야 하므로 이하로 정한다.
print(*ans)        