n = int(input()) # 몇개의 접시가 있는지

def hannoi(n, a, b, c):
    if n == 1:
        print(a, c) # 1개면 그냥 a에서 c로 옮기면 끝
    else: # 그 외에는
        hannoi(n - 1, a, c, b) # n-1개를 가운데에 옮기고
        print(a, c) # 나머지1개를 a에서 c로 옮김
        hannoi(n - 1, b, a, c) # 이제 그 가운데가 왼쪽자리라 생각하고 다시 반복.

print(2**n-1) # 총 옮기는 횟수는 프린트문에 있는것
hannoi(n, 1, 2, 3)        