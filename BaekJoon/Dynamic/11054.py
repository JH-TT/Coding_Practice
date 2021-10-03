from bisect import bisect_left

n = int(input())

seq = list(map(int, input().split()))
res = 1

def desc(a, num):
    desc_cnt = [-num]
    for i in range(len(a)):
        if -desc_cnt[-1] > a[i]:
            desc_cnt.append(-a[i])
        else:
            idx = bisect_left(desc_cnt, -a[i])
            desc_cnt[idx] = -a[i]

    return len(desc_cnt) - 1

asc_cnt = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[j] < seq[i]:
            asc_cnt[i] = max(asc_cnt[i], asc_cnt[j] + 1)

for i in range(n - 1, -1, -1):
    if i < n - 1:
        cnt = desc(seq[i+1:], seq[i])
        res = max(res, asc_cnt[i] + cnt)

print(res)

# 미리 증가하는 수열부터 만든다음
# 마지막 인덱스이전 부터 0까지 반복문을 돌면서
# 그 숫자부터 다시 감소하는 수열을 만들고
# 증가 하는 길이 + 감소하는 길이 - 1을 해준다.

# 다른 사람 풀이
import sys
from bisect import bisect_left


def find_longest(array):
    sub_array = [array[0]]
    cnt = []

    for a in array[1:]:
        if sub_array[-1] < a:
            sub_array.append(a)
        else:
            idx = bisect_left(sub_array, a)
            sub_array[idx] = a

        cnt.append(len(sub_array))

    return cnt


n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
increase = find_longest(A)
decrease = find_longest(A[::-1])

result = 1

for i, d in zip(increase, decrease[::-1]):
    result = max(result, i + d - 1)

print(result)
# 방식은 나랑 비슷하지만, 이 코드는 미리 증가, 감소를 전부 구한 후, 증가 + 감소 - 1을 하나씩 해줬다. 그러므로 이 코드가 훨씬 빠르다.