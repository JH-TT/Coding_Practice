def calc_time(s, e):
    s_h, s_m = map(int, s.split(":"))
    e_h, e_m = map(int, e.split(":"))
    h_diff = e_h - s_h
    m_diff = e_m - s_m
    return h_diff * 60 + m_diff

def check(info, m, time):
    idx = info.find(m)

    return False if idx == -1 else True

def change(info):
    ch = ['A#', 'C#', 'D#', 'F#', 'G#']
    ch_2 = ['a', 'c', 'd', 'f', 'g']
    for i in range(len(ch)):
        info = info.replace(ch[i], ch_2[i])
    return info

def solution(m, musicinfos):
    answer = [0, ""]
    m = change(m)
    for i in musicinfos:
        start, end, title, info = i.split(",")
        
        info = list(change(info))
        play_time = calc_time(start, end) # 총 플레이 타임 구함
        total_play = "".join(info) * (play_time // len(info)) + "".join(info)[:play_time % len(info)] # 플레이 동안 악보 저장.
        # 해당 멜로디가 있는지 확인
        if check(total_play, m, play_time):
            if play_time > answer[0]:
                answer = [play_time, title]

    return "(None)" if answer[1] == "" else answer[1]

# 샵 같은 것을 어떻게 처리할지 오래 고민했음.
# 계속 안되길래 뭐지 하다가 change 함수에서 ch랑 ch_2에 문자들이 빠져있었다. -> 알아채는데 가장 오래걸림