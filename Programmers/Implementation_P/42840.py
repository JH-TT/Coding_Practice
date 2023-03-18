def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i, cor in enumerate(answers):
        # 각 리스트를 순환하도록 % 기호를 이용한다.
        if cor == first[i%len(first)]:
            score[0] += 1
        if cor == second[i%len(second)]:
            score[1] += 1
        if cor == third[i%len(third)]:
            score[2] += 1
            
    answer = []
    high = max(score)
    
    for i, s in enumerate(score):
        if s == high:
            answer.append(i+1)
            
    return answer

# enumerate 상기 문제