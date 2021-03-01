# 2577번 : 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

a = int(input()) # 3개의 정수를 입력받는다.
b = int(input())
c = int(input())
d = str(a * b * c) # d에 abc를 곱한 값을 str로 저장한다.
for i in range(10): # 정수 i를 for문을 돌면서, str로 변환하고 count함수를 이용해 각 정수가 쓰인 개수를 출력한다.
    print(d.count(str(i)))