n = int(input())
a = list(map(int, input().split()))
a.sort() # a 정렬
m = int(input())
b = list(map(int, input().split()))


def bi(arr, tar, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == tar:
            return 1
        elif arr[mid] > tar:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in b:
    print(bi(a, i, 0, n - 1))