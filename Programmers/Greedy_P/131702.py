from itertools import product

def solution(clockHands):
    dx = [0, 1, 0]
    dy = [-1, 0, 1]
    n = len(clockHands)
    answer = 10**7
    total = 0
    for i in product([0, 1, 2, 3], repeat = n):
        arr = [a[:] for a in clockHands]
        res = 0
        for j in range(n):
            if i[j] == 0:
                continue
            arr[0][j] = (arr[0][j] + i[j]) % 4
            for h in range(3):
                nx = dx[h]
                ny = j + dy[h]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                arr[nx][ny] = (arr[nx][ny] + i[j]) % 4
            res += i[j]
        for a in range(1, n):
            for b in range(n):
                if arr[a-1][b] == 0:
                    continue
                spin = 4-arr[a-1][b]
                arr[a-1][b] = 0
                arr[a][b] = (arr[a][b] + spin) % 4
                for c in range(3):
                    nx = a + dx[c]
                    ny = b + dy[c]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    arr[nx][ny] = (arr[nx][ny] + spin) % 4
                res += spin
        if sum(arr[-1]) == 0:
            answer = min(answer, res)
            
    return answer

# 131703과 같은 방식
# 첫 행에서 나오는 경우의 수를 기준으로
# 아래 행은 위에 행 숫자를 보고 돌린다.