def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    mid = s // n
    r = s % n
    for i in range(n):
        if i < r:
            answer.append(mid + 1)
        else:
            answer.append(mid)
    answer.reverse()
    return answer

# 보통 수학적인 문제인 경우 생각한 방식이 맞는 경우가 많았다.
# 이번 문제같은 경우도 중간값들의 곱이 가장 클 것이라는 예상을 갖고 풀었더니 맞았다.
# n=2인 경우를 보면 x(n-x)가 나오기 때문에 n/2가 가장 큰 것을 볼 수 있기 때문이다.
# 그래서 중간값 mid와 나머지 r을 구한뒤
# r만큼 mid에 1을 더해서 넣어준다.
# 마지막엔 뒤집어준다.(오름차순으로 바꾸기 위함)