import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())))

    min = 10**9
    for i in range(n):
        l = i+1
        r = n-1
        while l <= r:
            mid = (l + r) // 2
            diff = s[i] + s[mid]
            if abs(k - diff) < min:
                min = abs(k - diff)
                cnt = 1
            elif abs(k - diff) == min:
                cnt += 1

            if diff > k:
                r = mid-1
            else:
                l = mid+1
    print(cnt)

# 왼쪽기준으로 하나씩 전부 찾는 방식.

# 다른 풀이
import sys
input = sys.stdin.readline

n=int(input())
for _ in range(n):
  a,b=map(int, input().split())
  data=list(map(int, input().split()))
  data.sort()
  start=0
  end=a-1
  answer=data[start]+data[end] # 현재 k값에 가까운 값
  count=0
  while start<end:
    tmp=data[start]+data[end]
    # 지금 tmp가 더 가까우면 answer를 tmp로 교환
    if abs(b-tmp)<abs(b-answer):
      count=0
      answer=tmp
    if abs(b-tmp)==abs(b-answer):
      count+=1
    # tmp가 b보다크면 -> 값을 줄인다.
    if tmp>b:
      end=end-1
    # 반대면 값을 키운다.
    else:
      start=start+1
  # 기본이 1이므로 0이면 1로 바꿔준다.
  if count==0:
    count=1
  print(count)
  
# 이까 로직 이렇게 했는데 왜 안됐지?
# 그래서 수정
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    s = sorted(list(map(int, input().split())))
    
    i, j = 0, n-1
    mini = s[i] + s[j]
    cnt = 0
    while i < j:
        diff = s[i] + s[j]
        if abs(k - diff) < abs(k - mini):
            mini = diff
            cnt = 0
        if abs(k - diff) == abs(k - mini):
            cnt += 1
        
        if diff > k:
            j -= 1
        else:
            i += 1
    if cnt == 0:
        cnt = 1
    print(cnt)