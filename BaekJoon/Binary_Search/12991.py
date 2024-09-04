from bisect import bisect_right

def binary(A, B, mid, i):
    start = 0
    end = len(A) - 1
    while start < end:
        mid_idx = (start + end + 1) // 2
        if A[mid_idx] * B[i] <= mid:
            start = mid_idx
        else:
            end = mid_idx - 1
    return start

def find_cnt(A, B, mid):
    res = 0
    for i in range(1, n + 1):
        res += binary(A, B, mid, i)
    return res

n, k = map(int, input().split())
A = [0] + sorted(list(map(int, input().split())))
B = [0] + sorted(list(map(int, input().split())))

start = A[1] * B[1]
end = A[-1] * B[-1]
res = 0
while start < end:
    mid = (start + end) // 2

    if find_cnt(A, B, mid) >= k:
        end = mid
    else:
        start = mid + 1
print(end)

# 이분탐색을 2번해야 풀 수 있는 문제
# k번째 수와 풀이는 비슷함