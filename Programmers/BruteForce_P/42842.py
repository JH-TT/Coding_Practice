def solution(brown, yellow):
    arr = []
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            arr.append([i, yellow // i])
    
    for i, j in arr:
        if 2 * (j + i) + 4 == brown: # 둘레 개수가 갈색이면 끝.
            return [j+2, i+2]