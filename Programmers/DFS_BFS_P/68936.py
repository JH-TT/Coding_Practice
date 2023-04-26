def solution(arr):
    return dfs(arr, len(arr), 0, 0)

def dfs(arr, level, x, y):
    target = arr[x][y]
    if level == 1 or check(arr, level, x, y):
        return [1, 0] if target == 0 else [0, 1] # 여기서 걸리면 아래를 가지않고 1또는 0만 리턴하면 된다. 그러면 한꺼번에 하나로 합쳐진것으로 계산된다.
    a = [0, 0]
    next_level = level // 2
    a = list(map(sum, zip(a, dfs(arr, next_level, x, y))))
    a = list(map(sum, zip(a, dfs(arr, next_level, x+next_level, y))))
    a = list(map(sum, zip(a, dfs(arr, next_level, x, y+next_level))))
    a = list(map(sum, zip(a, dfs(arr, next_level, x+next_level, y+next_level))))
    return a
    

def check(arr, level, x, y):
    target = arr[x][y]
    for i in range(level):
        for j in range(level):
            if i == 0 and j == 0:
                continue
            if target != arr[x+i][y+j]:
                return False
    return True
  
# 재귀를 이용해서 4등분씩 해 나간다.