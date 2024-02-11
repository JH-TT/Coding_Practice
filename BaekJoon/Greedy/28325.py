n = int(input())
small_room = list(map(int, input().split()))

# 계산을 할때는 쪽방이 있는 방부터 탐색하며 계산한다.
# 만약 그냥 1번부터 계산하게 되면, 쪽방이 아닌경우에 계산하기 귀찮아진다.
start_idx = -1
for i in range(n):
    if small_room[i] > 0:
        start_idx = i
        break

# 쪽방을 가진 방이 없는 경우
if start_idx == -1:
    if n == 1: print(n)
    else:
        print(n // 2)
else:
    res = small_room[start_idx]
    idx = (start_idx + 1) % n
    zero_cnt = 0
    while idx != start_idx:
        # 일단 쪽방의 개수부터 더한다.(어차피 쪽방이 없는 경우는 0이니까 res에 영향을 주지 않음)
        res += small_room[idx]        

        # 이때 쪽방을 가진 방을 만나면
        # 지금까지 연속으로 쪽방이 없는 방의 개수를 이용해서 res 값에 더한다.
        # 이때 연속으로 쪽방이 없는 방이 놓여있는 모습은 선형으로 있기 때문에 위와 다르게 +1을 한 뒤에 2로 나눠준다.
        # 당연히 쪽방이 없으면 zero_cnt만 1증가시키고 다음으로 넘어간다.
        if small_room[idx] != 0:
            res += (zero_cnt + 1) // 2
            zero_cnt = 0
        else:
            zero_cnt += 1
        idx = (idx + 1) % n
    # 여기까지 나오면 해당 idx는 start_idx로 돌아왔을것이고 이는 다시 쪽방을 가지는 방이기 때문에 다시 한번 연속으로 쪽방이 없는 방의 개수를 이용해서 res에 값을 더해준다.
    res += (zero_cnt + 1) // 2
    print(res)