def solution(park, routes):
    for i in range(len(park)):
        if "S" in park[i]:
            cor = [i, park[i].index("S")]
            break
    
    for route in routes:
        op, n = route.split()        
        n = int(n)
        if op == "E":
            if cor[1] + n >= len(park[0]):
                continue
            if "X" in park[cor[0]][cor[1]+1:cor[1]+n+1]:
                continue
            cor[1] += n
        elif op == "W":
            if cor[1] - n < 0:
                continue
            if "X" in park[cor[0]][cor[1]-n:cor[1]]:
                continue
            cor[1] -= n
        elif op == "S":
            if cor[0] + n >= len(park):
                continue
            if "X" in [park[cor[0]+i][cor[1]] for i in range(1, n+1)]:
                continue
            cor[0] += n
        else:
            if cor[0] - n < 0:
                continue
            if "X" in [park[cor[0]-i][cor[1]] for i in range(1, n+1)]:
                continue
            cor[0] -= n
    
    return [cor[0], cor[1]]
