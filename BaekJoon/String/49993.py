def solution(skill, skill_trees):
    answer = 0
    for si in skill_trees:
        idx = 0
        flag = True
        for s in si:
            if s not in skill:
                continue
            if skill[idx] != s:
                flag = False
                break
            idx += 1
        answer += flag
    
    return answer

# 중복 스킬이 주어지지 않으니 선형으로 하나씩 본다.
# 만약 해당 스킬이 스킬트리가 필요하다면
# 현재 가능한 skill과 같은 스킬이면 사용하고 아니면 다른 스킬트리로 넘어간다.