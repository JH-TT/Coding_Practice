import sys
input = sys.stdin.readline

def print_rest(x, y):
    flag = 1
    for i in range(y, -1, -1):
        if flag == 1: # 위쪽방향
            for j in range(x, 0, -1):
                print((j, i))
        else: # 아래쪽 방향
            for j in range(1, x+1):
                print((j, i))
        flag *= -1

for _ in range(int(input())):
    m, n = map(int, input().split())
    print(1)
    # 이 문제는 어떻게 출력할건지가 관건
    # 토로이드 그리드같은 경우는 반드시 사이클이 존재하기 때문에 1을 출력하고
    # ㄱ자로 훑고 ㄹ자로 왼쪽방향으로 진행하면 된다.
  
    # ㄱ자로 훑기
    for i in range(n):
        print((0, i))
    for i in range(1, m):
        print((i, n-1))
    # ㄹ자로 왼쪽 방향 훑기
    print_rest(m-1, n-2)