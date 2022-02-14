from collections import defaultdict

def solution(gems):
    s = set(gems)
    gem = set()
    visit = defaultdict(int)
        
    start = 0
    end = 0
    length = 100001 # gems의 길이가 최대 10만이기 때문.
    path = 0 # 다음 슬라이딩 윈도우의 시작 위치
    
    for i in range(len(gems)):
        flag = False
        for j in range(path, len(gems)):
            # 첫 보석이면 업데이트
            if visit[gems[j]] == 0:                
                gem.add(gems[j])
            visit[gems[j]] += 1
            
            # 만약 모든 보석이 있다면 길이를 측정 후 업데이트
            if len(gem) == len(s):
                if abs(i-j) < length:
                    start = i
                    end = j
                    length = abs(i-j)
                flag = True
                path = j # 다음 슬라이딩 윈도우 위치 저장
                break
        
        # 더 이상 구간을 좁힐 방법이 없는경우 끝냄.
        if not flag:
            break
        
        # 시작 위치 제거
        if gems[i] in visit:
            if visit[gems[i]] == 1:
                del visit[gems[i]]
                gem.remove(gems[i])
            else:
                visit[gems[i]] -= 1
        
        # 마지막 위치 제거
        if gems[path] in visit:
            if visit[gems[path]] == 1:
                del visit[gems[path]]
                gem.remove(gems[path])
            else:
                visit[gems[path]] -= 1
        
    return [start+1, end+1]