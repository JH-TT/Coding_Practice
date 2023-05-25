a = input()
cnt_b = a.count('b')

frame = "a" * (len(a)-cnt_b) + "b" * cnt_b
res = 1000
if len(a) < 3:
    print(0)
else:
    # aaabaabbab 이렇게 있으면 0번 인덱스 ~ len(a)-1까지, 1번부터 len(a)-1 넘어서 0번인덱스까지 ... 이런식으로 돌렸다 보면 된다. 
    # 그러면 굳이 a*2를 이용해서 문자열을 늘려서 사용안해도 됨.
    for i in range(len(a)):
        change_cnt = 0
        for j in range(len(a)):
            if a[(i+j) % len(a)] != frame[j]:
                change_cnt += 1
        res = min(res, change_cnt // 2) # 서로다른 2개가 1교환 하는 거라서 2로 나누고 비교한다. 
    print(res)