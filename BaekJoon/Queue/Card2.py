from collections import deque
n = int(input()) # 몇개의 카드가 있는지

array = deque(range(1, n + 1)) # 1부터 n까지의 카드를 배정한다.
while len(array) > 1: # 1장이 남을때까지 반복.
    array.popleft() # 제일 위에카드(인덱스0)을 버린다.
    array.append(array.popleft()) # 그 다음 위에 있는 카드는 가장 아래로 옮긴다.(인덱스0인 카드를 인덱스 n-1로 옮긴다.)
print(array[0]) # 마지막으로 남은 카드 출력.


# 이 코드는 시간초과가 일어난다.
# 이유는 리스트로 할때, pop을 하면 뽑아내고 나머지들을 앞으로 당겨오기때문에 시간이 더 걸리기 때문이다.
"""
import sys
input = sys.stdin.readline

n = int(input())

array = [x for x in range(1, n + 1)]
while len(array) > 1:
    array.pop(0)
    if len(array) == 1:
        break
    array.append(array.pop(0))
print(array[0])
"""
