from itertools import combinations
from bisect import *

# arr에서 find값의 개수를 구하는 함수.
# arr = [1, 4, 4, 6]이고, find = 4이면, bisect_right = 3, bisect_left = 1이 되어 4의 개수를 O(2log(len(arr)))만에 구할 수 있게된다.
# 그냥 count를 사용하면 시간초과발생함. arr의 길이가 n이 아닌 훨씬 길기때문이다.
def getcnt(arr, find):
    return bisect_right(arr, find) - bisect_left(arr, find)

# arr의 양수 부분수열의 합을 구하는 함수.
def subtotal(arr, sub_sum):
    for i in range(1, len(arr) + 1):
        for j in combinations(arr, i):
            sub_sum.append(sum(j))
    sub_sum.sort() # 이분탐색을 위해 정렬해 준다.

n, s = map(int, input().split())

arr = list(map(int, input().split()))
# 절반씩 나눠서해야 더 빨리 계산이 가능하다.
arr_1 = arr[:n//2]
arr_2 = arr[n//2:]

# 각 부분수열의 합을 저장할 리스트
arr_1_sum = []
arr_2_sum = []

# 부분수열의 합을 구해준다.
subtotal(arr_1, arr_1_sum)
subtotal(arr_2, arr_2_sum)
cnt = 0

# arr_1_sum의 원소하나 + arr_2_sum의 원소하나 = s를 찾는 방식을 이분탐색을 이용해서 구하는걸로 짠 것이다.
for i in arr_1_sum:
    find = s - i
    cnt += getcnt(arr_2_sum, find)

cnt += getcnt(arr_1_sum, s)
cnt += getcnt(arr_2_sum, s)

print(cnt)

# 총 풀이방식
# 일단 리스트를 절반 나누고
# 각 리스트의 부분수열 합을 구하고 오름차순 정렬한다.
# 그 다음 절반을 나눈 두 부분수열의 합 리스트에서 하나씩 꺼낸다음 합을 구하고 s랑 같으면 cnt를 증가시키는 방식을 이용.
# 위 방식을 먼저 arr_1_sum에서 하나 꺼낸다음(그 값을 i라 하자), s - i를 이분탐색을 이용해 bisect_right - bisect_left를 구하면
# s - i의 개수가 나오게 된다.(bisect_right를 하면 같은 값이 있는 경우, 오른쪽 인덱스를 리턴할 것이고 bisect_left를 그 반대기 떄문.)
# 마지막으론 arr의 원소중에 s랑 같은 값의 개수를 찾고 cnt에 더해준다.