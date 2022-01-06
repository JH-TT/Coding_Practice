def solution(r, c, q):
    answer = []
    arr = [[i for i in range(c*j+1, c*(j+1)+1)] for j in range(r)]
    
    
    for w, x, y, z in q:
        min_v = r * c
        # 각 테두리 별로 처리해준다.
        for i in range(z-2, x-2, -1):
            min_v = min(min_v, arr[w-1][i], arr[w-1][i+1])
            arr[w-1][i+1], arr[w-1][i] = arr[w-1][i], arr[w-1][i+1]
        for i in range(w, y):
            min_v = min(min_v, arr[i][x-1], arr[i-1][x-1])
            arr[i][x-1], arr[i-1][x-1] = arr[i-1][x-1], arr[i][x-1]
        for i in range(x, z):
            min_v = min(min_v, arr[y-1][i-1], arr[y-1][i])
            arr[y-1][i-1], arr[y-1][i] = arr[y-1][i], arr[y-1][i-1]
        for i in range(y-2, w-1, -1):
            min_v = min(min_v, arr[i+1][z-1], arr[i][z-1])
            arr[i+1][z-1], arr[i][z-1] = arr[i][z-1], arr[i+1][z-1]

        answer.append(min_v)        

    return answer
# 시계방향으로 돌리는것은 반시계방향으로 앞뒤를 바꿔가면 된다.    