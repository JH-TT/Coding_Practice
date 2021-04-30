# 이진탐색이긴 하지만 투포인터 느낌이 더 컸던 문제.
# 알고리즘 : 두 용액을 더한 특성값을 0보다 크면 왼쪽으로 1칸, 0보다 작으면 오른쪽으로 1칸, 0이면 종료하도록 만든다.
# 포인트는 두 특성값 합이 0이 아닐때 처리하는 방법인것 같다.

n = int(input())
arr = list(map(int, input().split()))

arr.sort() # 정렬

start, end = 0, n - 1
s = 10 ** 11
result = [] # 매 순간 마다 두 용액의 특성값의 합이 0에 가깝다고 판단될 때 마다 저장하는 곳(마지막으로 저장된 것이 답).

while start != end :
    a, b = arr[start], arr[end]
    if abs(s) > abs(a + b):
        s = a + b
        result.append([a, b])
    if a + b < 0:
        start += 1
    elif a + b > 0 :
        end -= 1
    else:
        result.append([a, b])
        break
print(result[-1][0], result[-1][1])