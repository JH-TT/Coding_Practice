from math import floor,ceil,sqrt

def solution(r1, r2):
    answer = 0
    for x in range(1,r2+1):
        max_y = floor(sqrt(r2**2-x**2)) # x**2 + y**2 = r**2 에서 변형된 형태 x에 값을 넣으면 y값이 나올텐데
                                        # y값이 정수가 아니면 소수점을 빼버린다.
        min_y = 0 if x>r1 else ceil(sqrt(r1**2-x**2)) # 위와 같은 방식이지만, r1의 범위를 벗어나면 점의 개수는 0개이다.
        answer += max_y-min_y+1

    return answer*4

# 이 문제는 쉽게 생각했으면 정말 쉽게 풀 수 있었던 문제.
# 내가 너무 처음에 어렵게 접근해서 시간 다 날린 문제
# x=1부터 r2까지 y축에 수평으로 잘랐을때 나오는 점의 개수를 더해가면서 계산했음