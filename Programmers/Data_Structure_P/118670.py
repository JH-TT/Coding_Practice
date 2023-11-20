from collections import deque

def solution(rc, operations):
    answer = []
    r = len(rc)
    c = len(rc[0])
    left = deque(rc[i][0] for i in range(r))
    right = deque(rc[i][c-1] for i in range(r))
    row = deque([deque(rc[i][1:c-1]) for i in range(r)])

    for op in operations:
        if op == "Rotate":
            row[0].appendleft(left.popleft())
            right.appendleft(row[0].pop())
            row[-1].append(right.pop())
            left.append(row[-1].popleft())
        else:
            row.appendleft(row.pop())
            left.appendleft(left.pop())
            right.appendleft(right.pop())

    for i in range(r):
        answer.append([left[i]] + list(row[i]) + [right[i]])

    return answer

# 이 문제는 선형으로 탐색하면 무조건 시간초과가 나오는 문제다.
# 움직이는 방식을 생각하면서 deque를 구현하는 것이다.
# 그래서 나는 left + row + right로 3 부분을 나눠서 최소한의 계산으로 쿼리를 실행하도록 했다.