# startswith함수 이용.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    
    
    return True
# 슬라이싱 이용.
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        if phone_book[i] in phone_book[i + 1][:length]:
            return False
    
    return True
# 이 문제는 정렬만 하면 서로 인접한 문자열끼리만 비교하면 된다.
# 만약 1번째 수가 2번쨰 문자열의 접두사가 아니라면, 3번쨰 문자열도 볼 필요없이 접두사가 되지 않기 때문이다.
# 정렬을 했기 때문에 1번째가 2, 3번째의 접두사가 아니라는건
# 2, 3번째 접두사를 수로 나타냈을때 1번쨰 수보단 크다는 소리이기 떄문.