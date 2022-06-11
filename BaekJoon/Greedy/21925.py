n = int(input())
arr = list(map(int, input().split()))

i, j = 0, 1
cnt = 0

while j < n:
    # 부분수열길이가 짝수이며 팰린드롬이면 개수 증가시키고 i, j 위치 변경.
    if arr[i:j+1] == arr[i:j+1][::-1] and (j - i + 1) % 2 == 0:
        cnt += 1
        i = j+1
        j += 1
    j += 1
  
print(cnt if cnt != 0 and i >= n else -1) # i가 n이상이고 cnt가 0이 아닐때만 개수 출력, 아니면 -1출력.

# 이게 골3정도는 아닌듯...