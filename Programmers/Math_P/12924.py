def solution(n):
    arr = list(range(1, n+1))
    i, j, cnt = 0, 0, 0
    while i <= j:
        if sum(arr[i:j+1]) < n:
            j += 1
        elif sum(arr[i:j+1]) > n:
            i += 1
        else:
            cnt += 1
            i += 1

    return cnt

# 투포인터로 상황에 맞게 포인터를 이동시켜서 n과 같으면 cnt를 증가시키는 방식을 이용함.