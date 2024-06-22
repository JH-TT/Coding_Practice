import sys
input = sys.stdin.readline

n, m = map(int, input().split())
seq = list(map(int, input().split()))


prefix_min = [0, seq[0]]
min_value = seq[0]
for i in range(1, n):
    if min_value < seq[i]:
        prefix_min.append(prefix_min[i] + min_value)
    else:
        prefix_min.append(prefix_min[i] + seq[i])
        min_value = seq[i]

res = -10e9
for i in range(m+1):
    right = seq[n-i-1]
    left = prefix_min[m+1-i] - prefix_min[m-i]
    res = max(res, right - left)

print(res)

# 이 문제는 구간최댓값, 구간최솟값을 O(1)만에 찾도록 하는것이 관건이다.
# 최대 M개를 지워서 최댓값을 알아내는건데, 문제의 시그마를 풀어쓰면 -A1 + AL이 되는것을 알 수 있다.
# 나는 prefix_min을 이용해서 풀었다. 가장 오른쪽 값은 고정하고 왼쪽중에 최솟값을 찾는 방식을 택했다.
# 내 풀이기준으로는 오른쪽에 i개를 지웠을때 가장 앞에 나오는 숫자를 고정한다.
# 그러면 최대 M-i개를 지워서 그 중에 최솟값을 알면 된다. 이 말은 A(1) ~ A(1+M-i)까지 구간에서 최솟값을 알면 된다.
# 이 때 구간 최솟값을 어떻게 구하냐
# 각 구간별로 최솟값을 누적합으로 구해나가면 된다.
# 예를 들어 1, 2, 3이 있으면 처음은 0, 다음은 1, 다음은 1 + min(1, 2), 마지막으로 1 + min(1, 2) + min(1, 2, 3) 이렇게 구하는 것이다.
# 그렇게 prefix_min을 만들어놓고
# 1~K까지의 구간에서 최솟값을 구하려면 prefix_min[k] - prefix[k-1]을 하면 된다.

# 구간 최댓값은 반대로 생각하면 된다. 오른쪽에서 왼쪽으로 최댓값만 누적합을 구해서 만들면 된다.