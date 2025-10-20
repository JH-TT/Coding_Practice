# 1. 중심점을 구한다.
# 2. 각 점에 대해 중심점과의 각도를 계산한다.
# 3. 그 각도 기준으로 정렬한다.
#   오름차순으로 정렬하면 반시계방향, 내림차순으로 정렬하면 시계방향 순서가 된다.
# 4. 좌표 리스트를 이용해서 신발끈 공식을 이용한다.

n = int(input())
pts = [list(map(int, input().split())) for _ in range(n)]

left = 0; right = 0
for i in range(n):
    left += pts[i][0] * pts[(i + 1) % n][1]

for i in range(n):
    right += pts[i][1] * pts[(i + 1) % n][0]

print(round(abs(left - right) / 2, 1))

# 다각형을 이루는 순서대로 주어진다고 했기 때문에 반시계방향 or 시계방향으로 주어진다는 것을 알 수 있다.
# 따라서 각도를 이용해서 정렬할 필요는 없음. 바로 신발끈공식 이용하면 됨.