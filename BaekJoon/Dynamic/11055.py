import copy

n = int(input())
arr = list(map(int, input().split()))
s = copy.deepcopy(arr) # 그대로 복사

for i in range(1, n): # 두번째 수부터 반복문 돌면서
    for j in range(i): # 첫번째부터 i-1번째 까지.
        if arr[j] < arr[i]: # 만약 i인덱스 이전에 작은 값이 있으면
            s[i] = max(s[i], s[j] + arr[i]) # 현재 값과, j인덱스의 값 + i인덱스의 값중에 더 큰것을 업데이트.
print(max(s))

# 11053과 비슷함.