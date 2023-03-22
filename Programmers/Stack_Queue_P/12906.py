def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
        else:
            if a != answer[-1]:
                answer.append(a)
    return answer