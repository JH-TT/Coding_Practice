import math


n = int(input())
arr = [True] * (n + 1)
cmd, *v = map(int, input().split())

if cmd == 1:
    # cmd가 2일때처럼 계산을 한다.
    answer = []
    for i in range(n-1, 0, -1):
        # v[0]이 0이라는것은 딱 맞게 떨어졌으니 그 이후는 내림차순이라는 의미이다.
        if v[0] == 0:
            break
        fac = math.factorial(i) # 2가지 경우, fac이 더크거나, 작거나같은경우
        if fac > v[0]:
            # fac이 더 크면 현재 채우지 않는 숫자중에 가장 작은 값을 넣는다.
            for j in range(1, n+1):
                if arr[j]:
                    answer.append(j)
                    arr[j] = False
                    break
        else:
            cnt = 0
            target = v[0] // fac + 1
            if v[0] % fac == 0:
                target -= 1
            for j in range(1, n+1):
                if arr[j]:
                    cnt += 1
                    if cnt == target:
                        answer.append(j)
                        arr[j] = False
                        v[0] -= fac * (target - (v[0] % fac != 0))
                        break
    # 남은 건 순서대로
    if v[0] == 0:
        for i in range(n, 0, -1):
            if arr[i]:
                answer.append(i)
                arr[i] = False
    else:
        for i in range(1, n+1):
            if arr[i]:
                answer.append(i)
                arr[i] = False
    print(*answer)
else:
    # h번째가 원래자리가 아니면 v[h]-1까지는 전부 순열을 돌았으니 (h-1)! 번이 추가된다.
    res = 0
    for i in range(n):
        if arr[v[i]]:
            cnt = 0
            for j in range(1, v[i]):
                if arr[j]:
                    cnt += 1
            arr[v[i]] = False
            res += cnt * math.factorial(n-i-1)
    print(res + 1)