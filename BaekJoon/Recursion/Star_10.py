import sys
num = int(input())

# 이 문제는 (x, y)좌표로 볼때, x와 y를 n으로 나눴을때,둘 다 나머지가 1이면 빈칸이다.
def star(i, j):
    while(i != 0):
        # 나머지가 1인 경우
        if(i % 3 == 1 and j % 3 == 1):
            sys.stdout.write(' ')
            return
        # 3으로 계속 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        i = i // 3
        j = j // 3
    sys.stdout.write('*') # 계속 나눠도 1이 안되면 "*"찍기.

for i in range(num):
    for j in range(num):
            star(i, j)
    sys.stdout.write('\n')

# Key Point!! -> 빈칸이 놓여야할 위치의 특징을 찾기!