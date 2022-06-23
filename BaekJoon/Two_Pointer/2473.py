import sys

n = int(input())
arr = sorted(list(map(int, input().split()))) # 이 문제는 정렬되지 않은 상태로 주어짐

res = []
diff = sys.maxsize
# arr의 첫번쨰 값을 먼저 정한다.
for i in range(n-2):
    start = i+1
    end = n-1
    hap = arr[i]
    # 이 while문은 용액(2467번) 문제처럼 풀이(용액 문제에선 기준이 0이라면 이 코드는 기준이 arr[i]라고 생각하면 됨)
    while start < end:
        sub_hap = arr[start] + arr[end]
        if abs(sub_hap + hap) < diff:
            res = [arr[i], arr[start], arr[end]]
            diff = abs(sub_hap + hap)
        if sub_hap > -hap:
            end -= 1
        elif sub_hap < -hap:
            start += 1
        else:
            break
print(*res)

# 앞서 풀었던 용액(2467번)과 풀이는 비슷함.
# 단 이번엔 3개의 용액이기 때문에 미리 한 용액을 정하고 나머지중에서 용액 문제 풀이처럼 2개를 정하는 방식이라 생각하면 됨.
# N이 5000까지밖에 안되기 때문에 N^2로 풀이 가능했음 단 Pypy로 가능.
# 함수를 이용하면 Python으로 시간초과가 안뜨는데 이는 함수의 local변수들은 런타임에 추가 될 수 없기 때문에 고정크기 array에 저장 될 수 있고,
# 빠르게 접근 할 수 이쓰나 글로벌 변수들은 런타임에 추가될 수 있기에 dict에 저장하기 때문에 저장/읽기에서 local 변수보다 느리다 라고함.
