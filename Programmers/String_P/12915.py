def solution(strings, n):
    return sorted(strings, key=lambda x : (x[n], x))

# 람다 함수를 설명하면 n번째 인덱스 기준으로 먼저 정렬한뒤, 만약 n번째 인덱스가 같으면 문자열 자체로 정렬하도록 했다.