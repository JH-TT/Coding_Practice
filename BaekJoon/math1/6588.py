import math, sys
input = sys.stdin.readline # 없으면 시간초과뜸


# 에라토스테네스의 체 실행
eratos = [True for i in range(1000001)]
eratos[0], eratos[1] = False, False

for i in range(2, int(math.sqrt(1000000)) + 1):
    if eratos[i] == True:
        j = 2
        while i * j <= 1000000:
            eratos[i*j] = False
            j += 1
# 에라토스테네스의 체 끝.

while 1:
    n = int(input())
    flag = True
    if n == 0: # 0 입력시 종료
        break
    for i in range(3, n//2 + 1, 2):
        if eratos[i] == True and eratos[n - i] == True:
            print(n, "=", i, "+", n-i)
            flag = False
            break    
    if flag: # 만약 홀수인 소수의 합으로 나타내지 못하면 아래문구를 출력
        print("Goldbach's conjecture is wrong.")