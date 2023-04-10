from collections import defaultdict

def solution(topping):
    answer = 0
    left = set()
    cnt = defaultdict(int)
    
    for t in topping:
        cnt[t] += 1
    
    for i in topping:
        left.add(i)
        cnt[i] -= 1
        if cnt[i] == 0:
            del cnt[i]
        if len(left) == len(cnt.values()):
            answer += 1
    
    return answer

# 그냥 list slice에 set, len 연산을 한번에 쓰면 시간초과발생
# 이를 효율적으로 처리하기 위해 left라는 set을 만들고 거기에 add를 해 나간뒤, len으로 개수를 비교하도록 구현
# left외에 오른쪽 부분은 cnt라는 dictionary로 구현해서 키 : 토핑, 값 : 개수 로 해서 for문을 돌면서 하나씩 left로 옮길때 마다 개수를 1씩 감소.
# 만약 0개가되면 del연산 수행으로 삭제시켜줌
# 그런뒤 left와 토핑개수 비교
# 이렇게하니 테스트 케이스 1번을 2000ms에서 7ms까지 확 줄였다 + 시간초과난 케이스도 최대 600ms까지 줄임