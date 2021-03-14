n, k = map(int, input().split())

a = []
b = list(map(int, input().split()))

for i in b:
    if len(a) < n:
      if i not in a:
          a.append(i)
    else:
        break
count = 0
for i in range(k):
    if b[i] in a:  # 현재 꽂혀있는 제품이면 넘기기.
        continue
    else: # 현재 꽂혀있지 않은 제품이라면 우선순위를 따져서 바꾸기.
        p = [] # 우선순위 넣을 공간.
        for j in range(n): # 꽂혀있는 제품들 중에 우선순위 확인
            pri = 0 # 우선순위
            for h in range(i + 1, k):
                if a[j] == b[h]: # 같은 제품을 만나면 반복문 종료하고 우선순위 append하고 다음 제품 확인.
                    break
                pri += 1
            p.append(pri)
        a[p.index(max(p))] = b[i] # 가장 나중에 사용하는 제품을 뺀다.
        count += 1
print(count)

# 이 문제는 마지막에 사용하는 제품을 우선순위로 두고 바꿔줘야하는것이다.