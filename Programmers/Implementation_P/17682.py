def solution(dartResult):
    score = []
    s = ''
    for d in dartResult:
        if d.isdigit():
            s += d
        elif d == "D":
            score.append(int(s) ** 2)
            s = ''
        elif d == "T":
            score.append(int(s) ** 3)
            s = ''
        elif d == "S":
            score.append(int(s))
            s = ''
        elif d == "*":
            if len(score) != 1:
                score[-2] *= 2
            score[-1] *= 2
        elif d == "#":
            score[-1] *= -1
        
    return sum(score)