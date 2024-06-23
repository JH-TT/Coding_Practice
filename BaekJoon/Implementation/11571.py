from collections import defaultdict
import sys
input = sys.stdin.readline

# a : 분자, b : 분모
for _ in range(int(input())):
    a, b = map(int, input().split())
    dict = defaultdict(int) # 지금까지 나온 숫자들 저장

    # 처음에 정수부분을 미리 구해놓는다.
    res = ""
    res += str(a // b) + "."
    a %= b

    l = len(res) # 소수점까지의 길이
    pos = 1
    while True:
        a *= 10
        # 반복시작
        if dict[a] != 0:
            # 괄호 감싸기
            res = res[:l+dict[a]-1] + "(" + res[l+dict[a]-1:] + ")"
            break
        # 없으면 숫자 저장
        dict[a] = pos
        pos += 1
        res += str(a // b)
        a %= b
    print(res)

# 순환소수가 되는 조건
# 같은 수를 나누는 상황이 나오면 순환소수가 된다.