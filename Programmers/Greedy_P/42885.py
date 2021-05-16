# 무게가 맞는 것 끼리 한 쌍으로 묶은 후, 나중에 사람수에서 n쌍을 빼주면 그것이 보트의 개수가 된다.
def solution(people, limit):
    answer = 0
    people.sort()
    
    start = 0
    end = len(people) - 1
    
    while start < end:
        if people[start] + people[end] <= limit:
            start += 1
            answer += 1
        end -= 1
    
    return len(people) - answer