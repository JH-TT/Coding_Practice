import copy

def solution(n, info):
    global gap, answer
    answer = [-1]
    gap = 0
    def dfs(r, idx, stack):
        global gap, answer
        if r == 0: # 화살을 다 쏘고 나면 점수 계산
            scores = Checkscore(info, stack)
            if (scores[1] > scores[0]) and (scores[1]-scores[0] >= gap):
                # 더 큰 차이로 이긴다면 answer업데이트
                if scores[1] - scores[0] > gap:
                    gap = scores[1] - scores[0]
                    answer = copy.deepcopy(stack)
                # 차이가 같으면 둘 중에 낮은 점수를 더 많이 맞춘거로 업데이트
                else:
                    for i in range(11):
                        if answer[10 - i] < stack[10 - i]:
                            answer = copy.deepcopy(stack)
                            break
                        if answer[10 - i] > stack[10 - i]:
                            break
        elif r > 0:
            for i in range(idx, 11):                
                if r - info[i] - 1 >= 0:
                    arrow = info[i] + 1
                else:
                    arrow = r
                stack[i] = arrow
                dfs(r-arrow, idx+1, stack)
                stack[i] = 0
                
    def Checkscore(ap, ry):
        apeach = 0
        ryan = 0
        for i in range(10):
            if ap[i] == 0 and ry[i] == 0:
                continue
                
            if ap[i] >= ry[i]:
                apeach += 10-i
            else:
                ryan += 10-i
                
        return [apeach, ryan]

    dfs(n, 0, [0]*11) # (남은 화살, 인덱스, 현재 라이언 과녁상태)를 넘겨준다.
    
    return answer