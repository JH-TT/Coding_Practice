# 정답
n = int(input())

num = list(map(int, input().split()))
O_Big_Num = [-1] * n

STACK = []
for i in range(n):
    while STACK and num[STACK[-1]] < num[i]:
        O_Big_Num[STACK[-1]] = num[i]
        STACK.pop()
    STACK.append(i)

print(*O_Big_Num)

# 내가 한 답 (시간초과)
n = int(input())

num = list(map(int, input().split()))
O_Big_Num = [-1] * n

STACK = []
for i in num:
    while STACK and STACK[-1] < i:
        O_Big_Num[num.index(STACK.pop())] = i
    STACK.append(i)

print(*O_Big_Num)

# 이 두 답은 sys라이브러리 사용.
# 간단한 설명
# 먼저 스택이 비어있거나, 스택의 탑부분이 현재 숫자보다 크면 넣어준다.
# 만약 스택의 탑 부분보다 큰 수가 오면, 스택의 탑 부분이 현재 수보다 클때까지 계속 빼면서 그 숫자의 오큰수를 현재 수로 지정한다.