import sys
input = sys.stdin.readline
n, h = map(int, input().split())

s = [] # 석순
j = [] # 종유석

# 석순 종유석 번갈아 나오니 짝 홀로 넣기.
for i in range(n):
    if i % 2 == 0:
        s.append(int(input()))
    else:
        j.append(int(input()))

s.sort() # 정렬
j.sort()

# x보다 긴 기둥의 개수 구하기
def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
           right = mid - 1
    
    return len(a) - (right + 1)

ans = n # 개똥벌레가 뚫을 기둥 최솟값
cnt = 0 # 그 최솟값의 개수

for i in range(1, h + 1):
    suck = binary_search(s, i - 1) # i - 1보다 큰 석순의 개수
    jong = binary_search(j, h - i) # h - i 보다 큰 종유석의 개수
    sum = suck + jong # 둘의 합
    if sum < ans:
        ans = sum
        cnt = 1 # 최솟값이 바뀌었으니 다시 카운트
    elif sum == ans: # 최솟값이 같으면 카운트 + 1
        cnt += 1
print(ans, cnt)