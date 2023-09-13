from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
start = []
# 종료시간을 기준으로 정렬한다.
# 종료시간 기준으로 회의의 순서가 정해지기 때문
info = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : x[1])

endMeeting = [x[1] for x in info]
startMeeting = [x[0] for x in info]
startEnd = sorted(list(set(startMeeting + endMeeting))) # 시작 + 끝 시간을 다 구한다.

simple = {}
for i, v in enumerate(startEnd):
    simple[v] = i

idx = len(startEnd)
dp = [0 for _ in range(idx)]
meetingIdx = 0

for i in range(idx):
    endTime = info[meetingIdx][1]
    # 만약 회의가 끝나는 시간이면
    if i == simple[endTime]:
        # 해당 회의 시작시간에 저장된 최대 인원수 + 현재 회의 인원수를 구한다.
        cur = dp[simple[info[meetingIdx][0]]] + info[meetingIdx][2]
        # 이전값과 비교해서 더 큰 값을 넣는다.
        dp[i] = max(dp[i-1], cur)
        meetingIdx += 1
    else: # 그 외에는 그냥 이전값을 그대로 이어간다.
        dp[i] = dp[i-1]

print(dp[-1])

# 좌표압축 + dp로 어려웠던 문제
# 웰논 문제라고 하네요
# 참고 블로그 : https://velog.io/@ok2qw66/BOJBOJ-19623-%ED%9A%8C%EC%9D%98%EC%8B%A4%EB%B0%B0%EC%A0%954