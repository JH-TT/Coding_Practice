from collections import defaultdict
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

prefix = [0]
for i in range(n):
    prefix.append(prefix[-1] + seq[i])

diff_prefix = defaultdict(int)
for i in range(1, n + 1):
    diff_prefix[prefix[i] - k * i] += 1

res = 0
for a in diff_prefix:
    res += diff_prefix[a] * (diff_prefix[a] - 1) // 2

if diff_prefix[0] > 0:
    res += diff_prefix[0]

print(res)

# 누적합을 구한뒤에
# 각 누적합 리스트마다 누적합길이 * k만큼 빼준다.
# 이때 누적합 인덱스a가 x고 인덱스 b도 x면, a+1 ~ b까지의 평균이 k가 된다는 의미!
# 쉽게말해, 누적합 길이 a인 경우의 평균이 x고 길이가 b인 평균도 x면 b > a 인 경우에 a+1번부터 b까지의 수열의 평균이 k라는 소리가 된다.
# 즉, 2개의 같은 값이 있으면 거기 사이에 평균 k의 수열이 존재한다는 의미가 된다.
# 만약 같은 값이 m개면 그 중에 2개를 고르면 평균k의 수열이 있다는 의미이므로 mC2가 된다.
# 그런데 값이 0인 경우는 해당 수열의 평균이 k가 된다는 의미이므로, 이 경우는 자기 자신도 개수를 더해준다.
# 즉, mC2로 전부 더한 다음에 0인 경우가 있으면 값이 0인 개수를 한 번 더 더해준다.(line 20~21)