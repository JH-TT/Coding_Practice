def solution(n, build_frame):
    def check_(x, y, a, arr):
        # 기둥을 조건
        if a == 0:
            if y == 0: # 바닥 위에 있는 경우
                return True
            elif (x > 0 and arr[y][x-1][1]) or arr[y][x][1]: # 보의 한쪽 끝 부분인 경우
                return True
            elif arr[y-1][x][0]: # 다른 기둥 위에 있는 경우
                return True
        else: # 보를 설치하는 경우
            # 양쪽 끝 부분이 기둥 위
            if arr[y-1][x][0] or arr[y-1][x+1][0]:
                return True
            # 양쪽 끝 부분이 다른 보와 동시에 연결
            elif x > 0 and arr[y][x-1][1] and arr[y][x+1][1]:
                return True
        return False
    
    answer = []
    # 기둥 : 0, 보 : 1
    arr = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]
    # print(arr)
    for bf in build_frame:
        x, y, a, b = bf
        # 삭제하는 경우, 해당 값을 0으로 변경하면 됨.
        if b == 0:
            arr[y][x][a] = 0 # 일단 삭제
            flag = True
            for i in range(n+1):
                for j in range(n+1):
                    if arr[i][j][0]:
                        flag &= check_(j, i, 0, arr)
                    if arr[i][j][1]:
                        flag &= check_(j, i, 1, arr)
            if not flag: # 어긋나는 부분 발견! 해당 작업 무효
                arr[y][x][a] = 1
            continue
        if check_(x, y, a, arr):
            arr[y][x][a] = 1
    # 마무리
    # 다시 한 번 하나씩 조건을 따지면서 answer에 넣어주면 된다.
    for i in range(n+1):
        for j in range(n+1):
            if arr[i][j][0]:
                answer.append([j, i, 0] * check_(j, i, 0, arr))
            if arr[i][j][1]:
                answer.append([j, i, 1] * check_(j, i, 1, arr))
                
    return sorted(answer)

# 순수 구현문제