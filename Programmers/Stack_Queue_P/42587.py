def solution(priorities, location):
    answer = 0

    while priorities:
        paper = priorities.pop(0)
        if priorities and paper < max(priorities):
            priorities.append(paper)
            if location == 0: # 지정된 값이 max가 아니면 다시 뒤로 간다.
                location = len(priorities) - 1
            else: # 그 외에는 앞으로 당겨진다.
                location -= 1
        else:
            answer += 1
            if location == 0:
                break
            location -= 1
            
    return answer