def solution(n):
    def hanoi(n, first, target, middle):
        if n == 1:
            answer.append([first, target])
            return
        hanoi(n-1, first, middle, target)
        answer.append([first, target])
        hanoi(n-1, middle, target, first)
    answer = []
    hanoi(n, 1, 3, 2)
    return answer

# 참고 링크
# https://velog.io/@jewon119/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B8%B0%EC%B4%88-%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98-%ED%83%91Tower-of-Hanoi

# 다른사람 풀이 (yield를 이용한 풀이)
def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans  # 2차원 배열을 반환해 주어야 합니다.

# 다른사람 풀이 (코드를 더욱 짧게)
def hanoi(f, t, m, n):
    if n == 0:
        return []

    return hanoi(f, m, t, n-1) + [[f, t]] + hanoi(m, t, f, n-1) # n-1개를 가운데로 보내는 경우 + 제일 큰 원판을 목표지점에 옮기는 경우 + n-1개를 가운데에서 목표로 옮기는 경우


def solution(n):
    return hanoi(1, 3, 2, n)