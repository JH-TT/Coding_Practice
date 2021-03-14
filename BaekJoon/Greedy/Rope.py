n = int(input()) # 로프의 개수
p = [] # 각 로프가 견디는 힘
w = [] # 여기에 큰 힘이 나올 수 있는 경우를 저장
for _ in range(n):
    p.append(int(input()))
p.sort(reverse = True) # 큰 것부터 보기위해 내림차순 정렬
for i in range(n):
    s = p[i] * (i + 1) # i+1개의 로프로 가장 큰 힘을 낼 수 있는 정도. 즉 [15, 10, 6]이라 하면, 1개로는 맨앞의 15가 가장 큰 힘이고, n개로는 상위n개의 힘중에 가장 작은 힘 * 로프의 개수가 가장 큰 힘이다.
    w.append(s)
print(max(w)) # 이중에 최댓값이 가장 큰 힘을 낼 수 있는 정도.