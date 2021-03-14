n = int(input()) # 도시개수 입력
dis = list(map(int, input().split())) # 도시거리 입력
city = list(map(int, input().split())) # 도시에 있는 주유가격 입력

s = city[0] # 첫도시 가격 지정
cost = s * dis[0] # 첫 도시에서 넣는 주유값
for i in range(1, len(dis)):
    if s < city[i]: # 그 도시 가격이 다음 도시 가격보다 값이 싸면 그대로 그 가격 이용
        cost += s * dis[i]
    else: # 다음 도시 주유값이 더 싸면 그 도시가격 이용
        s = city[i]
        cost += s * dis[i]
print(cost)