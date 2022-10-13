from collections import defaultdict

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))
arr3 = sorted(arr2)
arr4 = defaultdict(int)

i, j = 0, 0
while i < n and j < m:
    if arr[i] < arr[j]:
        i += 1
    elif arr[i] == arr[j]:
        arr4[arr[j]] = 1
        i += 1
        j += 1
    else:
        j += 1

for i in arr2:
    print(arr4[i], end=" ")

# n과 m의 범위가 50만이길래 그냥 찾는거로는 안되겠구나 싶어서
# 두 개의 배열을 정렬한 뒤 인덱스로 비교를 했다.
# 그러다가 해당 숫자가 있으면 딕셔너리를 이용해서 그 키값은 1로 설정.
# 그런 뒤 정렬을 하지않은 배열을 하나씩 보면서 딕셔너리 값 출력.