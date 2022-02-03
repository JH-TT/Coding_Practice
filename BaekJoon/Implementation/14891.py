def spin(a, b):
    if b == 1:
        n = a.pop()
        a = [n] + a
    else:
        n = a.pop(0)
        a.append(n)
    
    return a

def team(idx, d):
    direct = d
    # 왼쪽방향
    for i in range(idx, 1, -1):
        if sn[i][0] != sn[i-1][1]:
            direct *= -1
            gear[i-1] = spin(gear[i-1], direct)
        else:
            break
    direct = d
    # 오른쪽 방향
    for i in range(idx, 4):
        if sn[i][1] != sn[i+1][0]:
            direct *= -1
            gear[i+1] = spin(gear[i+1], direct)
        else:
            break

gear = [[0]] + [list(map(int, input())) for _ in range(4)]

k = int(input())
# 2, 6
for _ in range(k):
    sn = [[0]]
    for i in range(1, 5):
        sn.append([gear[i][6], gear[i][2]])
    idx, d = map(int, input().split())

    gear[idx] = spin(gear[idx], d)
    team(idx, d)

print(gear[1][0] + gear[2][0] * 2 + gear[3][0] * 4 + gear[4][0] * 8)