n = int(input())
p = list(map(int, input().split()))
p.sort()
weigh = p[0]
if weigh > 1:
    print(1)
else:
    for i in range(1, n):
        # p에서 i번째 수를 뽑았을 때 이 수가 지금까지 뽑은 수 보다 크되, 적어도 차이가 2 이상이어야 한다.
        # 만약 weigh가 20이고 뽑은게 21이면 weigh에 더할 수 있기 떄문이다.
        if weigh + 1 < p[i]:
            print(weigh + 1)
            exit(0)
        weigh += p[i]
    print(weigh + 1)