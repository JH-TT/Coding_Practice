# bisect 라이브러리 이용.
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

arr = list(map(int, input().split()))

result = bisect_right(arr, x) - bisect_left(arr, x)

if not result:
    print(-1)
else:
    print(result)

# bisect 라이브러리 이용x
def count_by_value(arr, x):
    n = len(arr)

    a = first(arr, x, 0, n - 1)

    if a == None:
        return 0
    
    b = last(arr, x, 0, n - 1)

    return b - a + 1

# 처음 위치를 찾는 이진 탐색 메서드.
def first(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 해당 값을 가지는 원소중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
        return mid
    # 중간점의 값 보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인.
    elif arr[mid] >= target:
        return first(arr, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인.
    else:
        return first(arr, target, mid + 1, end)

# 마지막 위치를 찾는 이진 탐색 메서드.(내부는 first와 동일)
def last(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 이부분이 조금 다름.
    if (mid == n - 1 or target < arr[mid + 1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target: # -> 같으면 오른쪽 탐색이라 여기선 그냥 작은지만 판단.(first에선 >= 임.)
        return last(arr, target, start, mid - 1)
    else:
        return last(arr, target, mid + 1, end)

n, x = map(int, input().split())
arr = list(map(int, input().split()))

count = count_by_value(arr, x)

if count == 0:
    print(-1)
else:
    print(count)