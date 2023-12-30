n = int(input())
res = 0
pos = []
for i in range(n):
    a, b, c, d = map(int, input().split())
    pos.append([d / a, 1])
    pos.append([b / c, -1])

pos.sort(key=lambda x : (-x[0], -x[1])) # 만약 시작점이자 마지막이면 시작점 먼저

cnt = 0
for t, point in pos:
    cnt += point
    res = max(res, cnt)

print(res)

# 기울기 기준으로 정렬한다.
# 시작점이면 +1, 끝 점이면 -1을 해준다.
# 그런데 만약 시작점과 끝 점이 겹치는 경우에는 시작점을 우선적으로 계산하고 그 뒤에 끝 점을 계산한다.
# ㄴ 문제에서 끝 점을 지나는 경우도 포함이라고 했기 때문
# 그렇게 계속 최댓값을 업데이트해서 결과를 출력한다.