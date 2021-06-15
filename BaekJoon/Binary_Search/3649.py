import sys
input = sys.stdin.readline

while 1:
    x = input() # 센티미터
    if x == "":
        break
    x = int(x) * 10000000
    n = int(input())
    lego = [int(input()) for _ in range(n)]
    lego.sort()

    start = 0
    end = n - 1

    while start < end:
        s = lego[start] + lego[end]

        if s == x:
            break
        elif s > x:
            end -= 1
        else:
            start += 1
    if n < 2:
        print("danger")
        continue
    if start == end:
        print("danger")
    else:
        print("yes", lego[start], lego[end])
# 이 문제에서 x를 문자로 받는 이유는 테스트 케이스를 어떻게 입력받는지 정보가 없었기 떄문에
# 그냥 엔터를 누르면 종료되는 형식이어서 엔터를 입력받기위해 문자열로 받는것이다.(안그럼 런타임에러뜸)        