from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    cnt = defaultdict(int)
    for w, n in zip(want, number):
        cnt[w] = n
    total_ = len(want)
    # 1일차 할인 리스트를 먼저 정리한다
    for i in range(10):
        if discount[i] in want:
            cnt[discount[i]] -= 1
            if cnt[discount[i]] == 0:
                total_ -= 1
    # (i+1)일차 ~ (마지막-1)일
    for i in range(len(discount)-10):
        # 먼저 해당이 되는지 확인
        if total_ == 0:
            answer += 1
        # 그 다음부터는 want에 있는 물품만 해당 과정을 처리한다.
        if discount[i] in want:
            cnt[discount[i]] += 1
            # 다시 생긴 경우
            if cnt[discount[i]] == 1:
                total_ += 1
        if discount[i+10] in want:
            cnt[discount[i+10]] -= 1
            # 전부 구매 가능해진 경우
            if cnt[discount[i+10]] == 0:
                total_ -= 1
    # 마지막날
    if total_ == 0:
        answer += 1

    return answer

# 투 포인터로 처음과 끝+1에 있는 물품을 확인하면서 선형으로 확인한다.

# want에 있는지 확인하는 방식을 딕셔너리로 사용해보기
from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    cnt = defaultdict(int)
    valid = defaultdict(int)
    for w, n in zip(want, number):
        cnt[w] = n
        valid[w] = 1
    total_ = len(want)
    for i in range(10):
        if discount[i] in want:
            cnt[discount[i]] -= 1
            if cnt[discount[i]] == 0:
                total_ -= 1
    # (i+1)일차
    for i in range(len(discount)-10):
        if total_ == 0:
            answer += 1
        if valid[discount[i]]:
            cnt[discount[i]] += 1
            # 다시 생긴 경우
            if cnt[discount[i]] == 1:
                total_ += 1
        if valid[discount[i+10]]:
            cnt[discount[i+10]] -= 1
            # 전부 구매 가능해진 경우
            if cnt[discount[i+10]] == 0:
                total_ -= 1
    if total_ == 0:
        answer += 1

    return answer

# 대부분은 이 방식이 조금 더 빨랐고, 몇몇 테스트 케이스는 위에 방식이 훨씬 빨랐다.