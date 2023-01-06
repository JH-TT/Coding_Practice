# 2023 카카오 블라인트
def solution(users, emoticons):
    answer = [0, 0]
    min_dis = min(i[0] for i in users)
    
    all_case = add_all_case([40, 30, 20, 10], len(emoticons))
    for c in all_case:
        if max(c) < min_dis:
            break
        total = 0
        members = 0
        for u in users:
            u_total = 0
            for e in range(len(emoticons)):
                if u[0] <= c[e]:
                    total += (emoticons[e] * (1 - c[e] / 100))
                    u_total += (emoticons[e] * (1 - c[e] / 100))
            if u_total >= u[1]:
                total -= u_total
                members += 1
        if answer[0] < members:
            print(c, total)
            answer = [members, total]
        elif answer[0] == members and answer[1] < total:
            print(c, total)
            answer = [members, total]
    
    return answer

def add_all_case(arr, n):
    case = []
    def com(a, level, track):
        if level == n:
            case.append(track)
            return
        for i in range(4):
            com(arr, level+1, track + [arr[i]])
    com(arr, 0, [])
    return case

# 할인율이 40, 30, 20, 10