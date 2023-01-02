import math

fac = math.factorial

def start():
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    if n == 1 or n == 2:
        return 0
    else:
        cnt = 0
        for i in range(n-2):
            s = i+1
            e = n-1
            # 양수면 어떤수를 더해도 양수다.(정렬했기 때문) 그러니 0이 될 수 없다.
            if arr[i] > 0:
                break
            # 2개를 찾는것이기 때문에 s와 e가 같아도 안된다.
            while s < e:
                sub_total = arr[s] + arr[e]
                if sub_total == -arr[i]:
                    left = 1
                    right = 1
                    # s의 값과 e의 값이 같으면 s-e+1 구간은 어떤 2개를 잡아도 합이 -arr[i]가 된다. 따라서 조합을 이용.
                    if arr[s] == arr[e]:
                        cnt += (e-s+1) * (e-s) // 2
                        break
                    # 왼쪽 부분과 오른쪽 부분 각각 같은수가 몇개인지 계산
                    while arr[s] == arr[s+1]:
                        left += 1
                        s += 1
                    while arr[e] == arr[e-1]:
                        right += 1
                        e -= 1
                    # 만약 왼쪽이 같은수가 n개 오른쪽은 m개이면
                    # n명중에 1명, m명중에 1명이 서로 짝이 된다.
                    # n명중에 1명 뽑는 경우의 후 : n
                    # m명 "                   : m
                    # 모든 경우의 수 : n*m
                    cnt += left * right
                    s += 1
                    e -= 1
                elif sub_total > -arr[i]:
                    e -= 1
                else:
                    s += 1
        return cnt
print(start())