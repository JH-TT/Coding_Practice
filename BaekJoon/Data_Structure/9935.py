str = list(input())
bomb = input()

stack = []
cnt = [] # 폭발 문자열 연속으로 정확한 개수

for s in str:
    stack.append(s)
    idx = -1 if not cnt else cnt[-1]

    # 만약 첫번째 문자와 같으면 0을 넣는다.
    if s == bomb[0]:
        idx = 0
        cnt.append(idx)
    # 마지막 다음 문자와 같으면 다음 인덱스번호를 넣는다.
    elif idx != -1 and s == bomb[idx+1]:
        idx += 1
        cnt.append(idx)
    else: # 그 외에는 -1을 넣는다.
        cnt.append(-1)

    if idx + 1 == len(bomb):
        for _ in range(len(bomb)):
            stack.pop()
            cnt.pop()

print("".join(stack) if stack else "FRULA")

# 스택만 알면 어렵지 않게 풀 수 있다.
# 너무 최적화에 신경써서 코드가 길었는데 단순하게 문자열 비교로 제거해도 충분히 통과가능하다