from itertools import combinations

def solution(numbers):
    answer = set()
    
    for case in combinations(numbers, 2):
        answer.add(sum(case))
    
    return sorted(list(answer))

# n이 최대 100까지고 2개만 뽑아서 구하니까 많아봐야 만개 정도다. 그러니 부르트포스로 풀었음.