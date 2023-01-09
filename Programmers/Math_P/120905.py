def solution(n, numlist):
    return list(filter(lambda x : x % n == 0, numlist))

# filter를 이요하면 쉽게 해당 함수에 맞게 거를 수 있다.