a = int(input())  # 몇개의 정수를 입력할지
array = list(map(int, input().split())) # 공백을 구분해 입력한 정수들을 리스트로 선언.

array.sort() # 배열을 오름차순으로 정렬한다.
print(min(array), max(array)) # 맨 앞이 최소값, 맨 뒤가 최댓값이 된다.