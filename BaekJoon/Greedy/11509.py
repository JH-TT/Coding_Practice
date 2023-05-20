from collections import defaultdict

# N의 최댓값이 100만이다. 따라서 최대 O(NlonN)까지만 허용한다.
N = int(input())

balloons = list(map(int, input().split()))
check = defaultdict(int) # 활성화된 풍선라인

res = 0
for i in range(N):
    # 비활성화면 현재 풍선을 기준으로 새로운 라인을 생성
    if check[balloons[i] + 1] == 0:
        check[balloons[i]] += 1
        res += 1
    else: # 들어갈수 있는 라인이 있으면 그 라인에 합류. 상위 풍선의 라인개수를 1감소.
        check[balloons[i]] += 1
        check[balloons[i] + 1] -= 1

print(res)