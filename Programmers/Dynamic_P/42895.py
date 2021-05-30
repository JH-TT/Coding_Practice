def solution(N, number):
    dp = []
    for i in range(1, 9): # 최솟값이 8까지.
        num = set() # 중복을 없애기 위해 집합이용.
        num.add(int(str(N)*i)) # N을 i개 이어붙인것.
        for j in range(0, i - 1):
            # 양끝인덱스에서 서로 사칙연산을 하고 num에 저장.
            for h in dp[j]:
                for k in dp[-j-1]:
                    num.add(h-k)
                    num.add(h+k)
                    num.add(h*k)
                    if k != 0:
                        num.add(h//k)
        if number in num: # 찾는 수가 num에 있으면 종료.
            return i
        dp.append(num)
    return -1 # 최솟값이 8보다 커지므로 -1 출력.