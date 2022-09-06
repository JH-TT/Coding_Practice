def time_to_sec(time):
    h, m, s = map(int, time.split(":"))
    return h*3600 + m*60 + s

def sec_to_time(sec):
    hours = sec // 3600
    mins = (sec % 3600) // 60
    secs = sec % 60
    return '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)

def solution(play_time, adv_time, logs):
    play_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)
    sec = [0 for _ in range(play_time + 1)]
    
    # 시작점과 끝점 표시
    for i in logs:
        s, e = map(time_to_sec, i.split("-"))
        sec[s] += 1
        sec[e] -= 1
    
    for i in range(1, len(sec)):
        sec[i] += sec[i-1]
        
    for i in range(1, len(sec)):
        sec[i] += sec[i-1]
    
    max_cnt = 0
    min_time = 0
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if max_cnt < sec[i] - sec[i - adv_time]:
                max_cnt = sec[i] - sec[i - adv_time]
                min_time = i - adv_time + 1
        else:
            if max_cnt < sec[i]:
                max_cnt = sec[i]
                min_time = i - adv_time + 1
    
    return sec_to_time(min_time)

# 참고 : https://dev-note-97.tistory.com/156