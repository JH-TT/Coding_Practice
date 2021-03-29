import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a, b = map(int, input().split()) # 인쇄할 문서 개수와, 궁금한 문서의 현재 인덱스
    array = list(map(int, input().split())) # a만큼 입력받는다.
    count = 0 # 몇번 pop됐는지(몇 번째 문서가 나갔는지)
    if len(array) == 1: # 1개면 그냥 1출력.
        print(1)
    else:
        index = b # 궁금한 문서 인덱스.
        while 1:
            if index == 0: # 궁금한 문서 차례.
                if array[index] == max(array): # 출력될 차례.
                    count += 1
                    print(count) # count증가시키고 출력.
                    break # 다음 테스트로 넘어감.
                else: # 가장 높은 우선순위가 아니라면.
                    c = array.pop(0)
                    array.append(c) # 뒤로 옮김.
                    index = len(array) - 1 # 가장 마지막 인덱스.
            else: # 순서가 아직 안됐을 때.
                if array[0] == max(array): # 현재 문서가 우선순위가 가장 높다면.
                    array.pop(0) # 배열에서 뺀다.
                    index -= 1 # 궁금한 문서 인덱스 1감소.
                    count += 1 # 출력 횟수 증가.
                else: # 현재 문서가 우선순위가 가장 높지 않다면.
                    c = array.pop(0) 
                    array.append(c) # 뒤로옮김.
                    index -= 1 # 궁금한 문서 인덱스 1 감소.

# 튜플로 변환.
# enumerate는 반복문 사용 시 인덱스 번호와 컬렉션의 원소를 튜플형태로 반환한다.
"""
array = list(map(int, input().split()))
q = [(i, index) for index, i in enumerate(array)]
print(max(q, key = lambda x : x[0])[0]) 
"""
# max람다 식으로 하니까 튜플 형태로 가장 큰 값과 그 큰 값의 위치가 나온다. ex) [1, 2, 4, 3]의 리스트가있다면, 위에처럼 max를 이용하면 (4, 2) 로 나온다.