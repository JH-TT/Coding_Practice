def solution(n):
    k = (n * (n + 1)) // 2
    answer = [0] * (k + 1)
    cnt = 0
    idx = 1
    answer[1] = 1
    num = 1
    
    while num < k:
        answer, num, idx = down(answer, k, idx, 1 if cnt == 0 else cnt * 2)
        answer, num, idx = right(answer, k, idx)
        answer, num, idx = up(answer, k, idx, n-cnt)
        
        cnt += 1
        
    return answer[1:]

def down(arr, k, cor, cnt):
    while cor + cnt <= k and arr[cor + cnt] == 0:
        arr[cor + cnt] = arr[cor] + 1
        cor += cnt
        cnt += 1
        
    return arr, arr[cor], cor

def right(arr, k, cor):
    while cor + 1 <= k and arr[cor + 1] == 0:
        arr[cor + 1] = arr[cor] + 1
        cor += 1
    return arr, arr[cor], cor

def up(arr, k, cor, cnt):
    while 1 < cor - cnt and arr[cor - cnt] == 0:
        arr[cor - cnt] = arr[cor] + 1
        cor -= cnt
        cnt -= 1
    return arr, arr[cor], cor

# 그냥 각 방향마다 규칙만 찾으면 됨.
# 그래프로 푼 사람도 있었음.

# 그래프 느낌으로
def solution(n):
    [row, col, cnt] = [-1, 0, 1]
    board = [[None] * i for i in range(1, n+1)]
    for i in range(n):
        for _ in range(n-i):
            if i % 3 == 0:
                row += 1
            elif i % 3 == 1:
                col += 1
            else:
                row -= 1
                col -= 1
            board[row][col] = cnt
            cnt += 1
# 로직은 나랑 비슷한데 이게 더 깔끔한듯
# 마지막은 chain써서 합쳤음