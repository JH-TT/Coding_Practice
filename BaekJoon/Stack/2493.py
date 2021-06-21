import sys
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
ans = [0 for _ in range(n)]
a = []

# 조건에 만족하지 않으면 계속 a에 i(인덱스)를 집어넣고
# 조건이 되면 빼면서 ans에 값을 넣어준다.
for i in range(n - 1, -1, -1):
    while a and top[a[-1]] < top[i]:
        ans[a.pop()] = i + 1
    a.append(i)

print(*ans)
# 이건 인터넷을 보고 한거지만 내가 했던 방식과는 동일. 단지 나는 인덱스가아닌 값으로 해결하려 하다보니
# index, copy함수 같은걸 사용하게되어 시간초과가 나왔다.