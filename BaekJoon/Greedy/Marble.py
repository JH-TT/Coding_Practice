n = int(input())

b = list(map(int, input().split()))
i = b.index(max(b)) # b중에 가장 큰 수가 있는 인덱스를 호출

for k in range(n):
    if k == i: # 가장 큰 수가 있는 인덱스면 넘기기.
        continue
    b[k] += b[i] # 가장 큰 수를 제외한 나머지에 가장 큰 수를 더해준다.
print(sum(b) - b[i]) # 리스트의 총합에서 가장 큰 수를 빼준다.