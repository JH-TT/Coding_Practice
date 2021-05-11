from bisect import bisect_right, bisect_left
from collections import Counter
# 방법 1, 2, 3은 전부 이것이 코테다에 나오는 방법이다.
# 1, 2번의 자세한 설명은 책 or It's_COTE 카테고리에서 확인 바란다.
# Method 1 : binary Search 이용.
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

def cnt(arr, x):
    n = len(arr)
    a = first(arr, x, 0, n - 1)
    if a == None:
        return 0
    b = last(arr, x, 0, n - 1)
    return b - a + 1

def first(arr, tar, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or tar > arr[mid - 1]) and arr[mid] == tar:
        return mid
    elif arr[mid] >= tar:
        return first(arr, tar, start, mid - 1)
    else:
        return first(arr, tar, mid + 1, end)

def last(arr, tar, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if (mid == n - 1 or tar < arr[mid + 1]) and arr[mid] == tar:
        return mid
    elif arr[mid] > tar:
        return last(arr, tar, start, mid - 1)
    else:
        return last(arr, tar, mid + 1, end)

for i in b:
    print(cnt(a, i), end=" ")

# Method 2 : bisect 이용.

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = list(map(int, input().split()))

def cnt(arr, le, ri):
    right = bisect_right(arr, ri)
    left = bisect_left(arr, le)
    return right - left

for i in b:
    print(cnt(a, i, i), end=" ")

# Method 3 : Counter 이용
n = int(input())
a = Counter(input().split())
m = int(input())
b = list(input().split())

for i in b:
    print(a[i], end = " ")

# 숏코딩
_,i,_,q=open(0) # open이용해서 n -> _ 그담 n개의 숫자들 -> i, m -> _ m개의 숫자들 -> q 에 저장.
d={} # d사전형 리스트 생성.
for x in i.split():
    d[x] = d.get(x, 0) + 1 # d에서 x를 찾아서 키값반환, 없으면 0출력.
for x in q.split():
    print(d.get(x, 0)) # d에서 x를 찾아 키값 반환.