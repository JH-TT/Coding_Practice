def time_to_sec(endTime):
    t = endTime.split(":")
    h = float(t[0])
    m = float(t[1])
    s = float(t[2])
    return h * 3600 + m * 60 + s

def solution(lines):
    answer = 0

    info = []

    for line in lines:
        timeInfo = line.split()

        endTime = timeInfo[1] # 처리 마지막 시간
        runTime = float(timeInfo[2][:-1]) * 1000 # 처리가 걸린 시간

        timeSec = time_to_sec(endTime) * 1000 # 끝나는 시간대를 초단위로 변경
        info.append([timeSec - runTime + 1, timeSec]) # 시간 정보를 넣는다.

    # 시작 시간대를 기준으로 정렬한다.
    info.sort()

    # 완탐 시작(N이 2000이하라서 N ^ 2까지는 무난하게 돈다.)
    for i in range(len(info)):
        s = info[i][0] # 시작 시간을 기준으로 본다.
        oneSecLater = s + 999 # 1초후 시간
        cnt = 0 # 총 처리 개수
        for task in info[i:]:
            # 시작 시간이 1초후보다 뒤면 더이상 볼 필요 없다.
            if oneSecLater < task[0]:
                break
            cnt += 1
        answer = max(answer, cnt)

    # 끝나는 시간 기준으로도 확인해 본다.
    info2 = sorted(info, key = lambda x : x[1]) # 끝나는 시간 기준 정렬

    # 완탐 시작
    for i in range(len(info2)):
        e = info2[i][1] # 끝 시간을 기준으로 본다.
        oneSecLater = e + 999 # 1초후 시간
        cnt = 0 # 총 처리 개수
        for task in info2[i:]:
            # 시작시간이 oneSecLater를 넘으면 continue
            if oneSecLater < task[0]:
                continue
            cnt += 1
        answer = max(answer, cnt)

    return answer

# 카카오가 좋아하는 시간 문자열 파싱문제
# 기준을 잡고 완탐돌리면 되는 간단한 문제였다.
# "어떤 상황에 있어야 처리량으로 인정되는지" 그림을 그려보면 바로 풀이가 떠오르게 되는 문제였다.
# 그래서 시작시간 기준으로 정렬해서 1초범위에 있는 최대 작업량을 구하고
# 끝나는 시간 기준으로 정렬해서 1초범위에 있는 최대 작업량을 구한뒤에
# 둘 중 큰 값을 리턴하는 방식으로 풀었다.
# 아무리 느려도 20ms에 다 풀린문제