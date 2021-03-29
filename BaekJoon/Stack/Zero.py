import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    a = int(input())
    if a == 0: # 0일땐 pop을한다.
        arr.pop()
    else: # 아닌경우엔 push
        arr.append(a)
print(sum(arr))