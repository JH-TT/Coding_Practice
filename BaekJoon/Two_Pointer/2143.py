import bisect

T = int(input())
n1 = int(input())
a = list(map(int, input().split()))
n2 = int(input())
b = list(map(int, input().split()))

a_l = [0]
b_l = [0]

for i in a:
    a_l.append(a_l[-1] + i)

for i in b:
    b_l.append(b_l[-1] + i)

b_sub_sum = []
for i in range(len(b_l) - 1):
    for j in range(i + 1, len(b_l)):
        b_sub_sum.append(b_l[j] - b_l[i])

b_sub_sum.sort()

cnt = 0
for i in range(len(a_l) - 1):
    for j in range(i + 1, len(a_l)):
        a_sub_sum = a_l[j] - a_l[i]
        b_left_idx = bisect.bisect_left(b_sub_sum, T - a_sub_sum)
        b_right_idx = bisect.bisect_right(b_sub_sum, T - a_sub_sum)

        if b_left_idx == b_right_idx:
            continue

        cnt += b_right_idx - b_left_idx

print(cnt)

# a의 누적합을 구한다.
# b의 누적합을 구한다.
# b의 누적합 리스트를 이용해서 b의 모든 부 배열합을 구한다.
# a의 부 배열합을 가져온뒤 T - a부배열합을 b의 모든 부 배열합에서 이진탐색으로 찾는다.
# left와 right를 구하면 right-left가 T - a부배열합의 개수가 된다.