def solution(line):
    cor = []
    # 절댓값 최대가 10**15이기 때문에 10**15보다 큰 수로 지정한다.
    max_x = -10**16
    min_x = 10**16
    max_y = -10**16
    min_y = 10**16

    # 두 함수의 해(x, y)를 구한다.
    for i in range(len(line)-1):
        A, B, E = line[i]
        for j in range(i+1, len(line)):
            C, D, F = line[j]
            # 0으로 나누는 경우를 거르기위해 try문을 사용
            try:
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)
                # 정수가 아니면 넘긴다.
                if x != int(x) or y != int(y):
                    continue
                x = int(x)
                y = int(y)
                max_x = max(max_x, x)
                min_x = min(min_x, x)
                max_y = max(max_y, y)
                min_y = min(min_y, y)
                cor.append([x, y])
            except:
                continue
    # 최소폭을 구해서 2차원 리스트로 만든다.
    answer = [["." for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

    for c in cor:
        # 원점기준으로 평행이동시킨다.
        y = abs(c[1] - max_y)
        x = abs(c[0] - min_x)
        answer[y][x] = "*" # 그 부분은 *으로 바꾼다.
    answer = ["".join(re) for re in answer]
    
    return answer