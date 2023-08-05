from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    cnt = deque()
    # 셔틀버스가 절대 태울 수 없는 크루는 뺀다.
    for ti in timetable:
        if check_time(ti, n, t):
            cnt.append(time_to_minute(ti))
    time = 9 * 60
    now = 0
    board = m
    # 확인 시작
    for i in range(n):
        # 이미 다 태운거면 종료
        if not cnt:
            break
        board = m
        while cnt:
            now = cnt[0]
            if now > time:
                break
            board -= 1
            cnt.popleft()
            if board == 0:
                break
        time += t
    # 크루가 남은 경우
    if cnt:
        # 마지막으로 탄 크루보다 1분전이 최대다
        now -= 1
    else:
        # 막차가 아니면 무조건 막차시간이 정답
        if time-t != 9 * 60 + (n-1) * t:
            now = 9 * 60 + (n-1) * t
        else: # 막차인 경우엔 버스에 자리가 있냐 없냐로 나뉜다.
            # 자리가 있으면 막차가 답이 된다.
            if board != 0:
                now = time-t
            else: # 자리가 없으면 마지막 승객 1분전이 정답
                now -= 1
          
    return minute_to_time(now)

def check_time(t1, n, t):
    h, m = map(int, t1.split(":"))
    if 9 * 60 + (n-1) * t < h * 60 + m:
        return False
    return True

def time_to_minute(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def minute_to_time(s):
    h = s // 60
    m = s % 60
    if h < 10:
        h = "0" + str(h)
    if m < 10:
        m = "0" + str(m)
    return str(h) + ":" + str(m)

# 시간 가공하는 문제는 정말 귀찮다...