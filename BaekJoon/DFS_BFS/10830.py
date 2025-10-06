from collections import defaultdict

global d
d = defaultdict(list) # 캐시를 위한 딕셔너리

def multi(a, b):
    an = len(a)
    bn = len(b[0])
    
    res = [[0 for _ in range(bn)] for _ in range(an)]
  
    for i in range(an):
        for j in range(bn):
            total = 0
            for k in range(bn):
                total += (a[i][k] * b[k][j])
            res[i][j] = total % 1000

    return res

def calc(arr, n):
    global d

    if n in d:
        return d[n]
  
    if n == 1:
        return arr
    if n == 2:
        res = multi(arr, arr)
        d[2] = res
        return res

    if n % 2 == 0:
        res = multi(calc(arr, n // 2), calc(arr, n // 2))
        d[n] = res
        return res
    else:
        res = multi(calc(arr, n // 2), calc(arr, n // 2 + 1))
        d[n] = res
        return res

n, b = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] %= 1000

for res in calc(arr, b):
    print(*res)