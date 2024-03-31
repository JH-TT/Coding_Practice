import sys
from itertools import product
input = sys.stdin.readline

n = int(input())
balls = sorted(list(map(int, input().split()))) # 공의 위치들
t = int(input())

# 방향 모든 경우의 수 -1은 왼쪽, 1은 오른쪽이다.
dir = [-1, 1]

all_case = product(dir, repeat = n)
cnt = 0
for case in all_case:
    for i in range(n):
        for j in range(i+1, n):
            # 서로 나가는 방향이면 무시
            if case[i] == -1 and case[j] == 1: continue
            # 서로 같은 방향이면 무시
            if case[i] == case[j]: continue
            # 시간내에 만나지 못하는 경우 무시
            if balls[j] - balls[i] > t * 2: continue
            cnt += 1
print(cnt / (2 ** n))

# 핵심은 공이 서로 부딪히면 방향만 바뀌고 속도는 일정하다는 점
# 크기가 0이라는 점
# 이를 종합하면 예를 들어 5번 위치 8번 위치 공이 있고 이들 공에게 5번 8번이라는 이름을 부여하자.

# 만약 둘이 만나는 방향으로 가다가 부딪혀서 5번공은 6번위치 8번공은 7번위치에 방향이 반대인 상태로 있게 되는데
# 이는 서로 부딪히지 않고 지나가는 개념으로 봐도 무방하게 된다.
# 즉 둘이 지나쳐서 5번 공은 7번위치 8번공은 6번위치로 된 것과 같다. (공이 서로 다르다는 점)

# 따라서 서로 다른 공을 보고 일직선으로 쭉 이동한다는 가정하에 t초이내로 만나는지만 확인하면 된다.