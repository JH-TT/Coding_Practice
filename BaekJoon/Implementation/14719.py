h, w = map(int, input().split())
block = list(map(int, input().split()))

long = max(block)
ans = h * w - sum(block)

if long != h:
    ans -= (h - long) * w

# 가장 긴 벽의 위치 탐색
for i in range(w):
    if block[i] == long:
        l = i
        break
for j in range(w - 1, -1, -1):
    if block[j] == long:
        r = j
        break
l_index = l
r_index = r
l_max = long
r_max = long

# 왼쪽(처음에 가장 큰 블럭이 맨 왼쪽에 있으면 왼쪽을 볼 필요 없음.)
while l_index > 0:
    l_sub_block = block[:l]
    l_sub_max = max(l_sub_block)
    for i in range(l-1, -1, -1):
        if block[i] == l_sub_max:
            index = i
            break            
    ans -= (l_max - l_sub_max) * l
    if index == 0:
        break
    l = index
    l_max = l_sub_max
# 오른쪽(왼쪽과 마찬가지로 큰 블럭이 맨 오른쪽에 있으면 오른쪽을 볼 필요 없음.)
while r_index < w - 1:
    r_sub_block = block[r + 1:] # 가장 큰 블럭을 제외한 나머지 블럭의 리스트를 r_sub_block 이라함.
    r_sub_max = max(r_sub_block) # 그 중에 가장 큰 블럭을 r_sub_max라 함.
    for i in range(r + 1, w): # 그 블럭의 인덱스 탐색.
        if block[i] == r_sub_max:
            index = i
            break
    ans -= (r_max - r_sub_max) * (w - r - 1) # (이전의 가장 큰 높이 - 현재 가장 큰 높이) * (이전의 가장 큰 블럭 이후의 블럭의 개수)
    if index == w - 1:
        break
    r = index
    r_max = r_sub_max
print(ans)

# 다른사람 풀이.
H, W = map(int, input().split()) # 세로, 가로
blocks = list(map(int, input().split()))
rain = 0
for i in range(1, W):
    L_max = max(blocks[0:i]) # 현재블럭의 왼쪽들 중에 가장 높은 층수
    R_max = max(blocks[i:]) # 현재블럭 포함 오른쪽들 중에 가장 높은 층수
    diff = min(L_max, R_max) # 둘 중에 작은거
    if blocks[i] < diff: # 현재 블럭이 더 작다면 계산 실행.(크면 비가 찰 수 없다.)
        rain += (diff - blocks[i])
print(rain)