def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i - 1)
        elif i + 1 in lost_set:
            lost_set.remove(i + 1)


    return n - len(lost_set)

# 도난당한 학생이 여분을 갖고있으면 그냥 도난당하지 않고 여분을 갖지않은 학생으로 분류하고 나머지를 처리하면 된다.