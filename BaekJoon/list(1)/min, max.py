# 10818번 : N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

a = int(input())  # 몇개의 정수를 입력할지
array = list(map(int, input().split())) # 공백을 구분해 입력한 정수들을 리스트로 선언.

print(min(array), max(array)) # min은 최솟값을, max는 최댓값을 출력한다.
