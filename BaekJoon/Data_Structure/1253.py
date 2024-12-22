# 딕셔너리를 이용한 풀이
from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
d = defaultdict(int) # key : 숫자, value : 현재 존재하는 개수
arr = list(map(int, input().split()))
check = defaultdict(lambda: False)
for v in arr:
    d[v] += 1

res = 0
for i in range(n):
    for j in range(i + 1, n):
        if i == j: continue
        if check[arr[i] + arr[j]]: continue
        if d[arr[i] + arr[j]] == 0: continue # 당연히 없는 숫자면 넘긴다.
        # 둘 다 0이면 0이 몇개인지 확인하고 3개이상이어야만 더하고 그 외에는 스킵한다. (왜냐하면 0이 아닌숫자로 0을 만들 수 있기 때문)
        if arr[i] == 0 and arr[j] == 0:
            if d[0] > 2:
                res += d[0]
                check[0] = True
                continue
            else:
                continue
        # 둘 중에 0이 한 개면 다른 하나가 1개만 있는지 확인한다.
        if arr[i] == 0 or arr[j] == 0:
            if d[arr[i] + arr[j]] > 1:
                res += d[arr[i] + arr[j]]
                check[arr[i] + arr[j]] = True
                continue
            else:
                continue
        # 그 외에는 그냥 있는지만 체크한다.
        res += d[arr[i] + arr[j]]
        check[arr[i] + arr[j]] = True
print(res)
# 딕셔너리를 이용하는 풀이 중요한 부분은 0의 경우 2개를 다 사용해도 값이 같은수가 남아있다면 해당 숫자는 모두 만들 수 있다는 부분을 이용함.
# ex) 0 0 0의 경우 0 2개를 사용해도 다른 0이 존재하기 때문에 3개의 0을 전부 만들 수 있다.
# ex) 0 1 1의 경우 0 1을 사용해도 다른 1이 존재하기 때문에 1을 2개 전부 만들 수 있다.