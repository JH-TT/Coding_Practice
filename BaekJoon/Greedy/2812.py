n, k = map(int, input().split())
number = list(map(int, input()))
stack = [number[0]]

a = 0
for i in range(1, n):
    # 스택의 탑부분이 number의 i인덱스보다 작으면 pop한다.
    # 이때 pop을 한다는것은 제거하는 것이니 제거 횟수를 나타내는 a의 값을 1 증가시킨다.
    while stack and stack[-1] < number[i] and a < k:
        stack.pop()
        a += 1
    stack.append(number[i])

while a < k:
    stack.pop()
    a += 1

for i in range(len(stack)):
    print(stack[i], end="")