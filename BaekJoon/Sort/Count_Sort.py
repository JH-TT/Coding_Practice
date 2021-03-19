# 계수정리를 이용(가장큰 데이터와 가장 작은 데이터의 차가  100만 미만일때 유용)
import sys
input = sys.stdin.readline # 입력 빨리 받기 위함.

n = int(input())
a = [0 for i in range(10000 + 1)] # 문제에서 최대 10000까지만 나온다 했으니 일단 0부터 10000까지 0으로 초기화.

for i in range(n): # 입력 횟수를 돌면서 입력한 값이 인덱스가 되고, a의 그 인덱스값이 1증가하는 식이다.
    a[int(input())] += 1

for i in range(1, 10000 + 1): # 1이상 10000이하이므로 for문도 1부터 로 지정한다.
    for j in range(a[i]): # a배열의 i인덱스 값만큼 i를 출력. a[1] = 2 면 1을 2번 출력.
        print(i)
# 계수정렬은 메모리초과를 방지하기위해 사용한다.