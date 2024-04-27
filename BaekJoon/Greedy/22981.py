import sys, math

n, k = map(int, input().split())
v = sorted(list(map(int, input().split())))

res = sys.maxsize

for i in range(1, n):
    l_min = v[0]
    r_min = v[i]
    tran_time = l_min * i + r_min * (n - i)
    res = min(res, k // tran_time + (k % tran_time != 0))

print(res)

# 이 문제는 적절하게 팀을 나눠서 최소한의 시간으로 K개의 박스를 옮기도록 하는 문제였다. 따라서 그리디 문제이다.
# 그런데 이 문제는 가장 느린사람 기준으로 팀 처리속도가 결정되기 때문에
# 최소 시간으로 하려면 최솟값이 최대한으로 크게 구성원은 많게 해야한다.
# 그런데 v배열에서 최솟값은 어느 한 팀의 처리속도 기준이 되기 때문에
# 나머지 한 팀의 최솟값과 구성원 수에 따라 결정되게 된다.
# 최솟값이 최대이면서 구성원이 최대한으로 많으려면 v값을 오름차순 정렬한뒤
# v의 최솟값이 아닌 다른 숫자들을 다른 한 팀의 최솟값이라 두고 계산하면 된다.
# math.ceil 썼다가 특정 부분에서 답이 맞제 안나와서 위의 방식대로 수정하고 했음