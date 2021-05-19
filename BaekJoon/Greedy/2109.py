n = int(input())
a = []
for _ in range(n):
    p, d = map(int, input().split())
    a.append([d, p])
temp = []
total = 0
# 기간을 기준으로 정렬, 기간이 같으면 비용기준 정렬.
a.sort(key=lambda x:(x[0], x[1]))
# 일단 페이들을 넣다가 만약 temp의 길이가 그 페이를 받는 기간보다 길면
# 현재 temp에서 최솟값을 제거.
for i in range(n):
    total += a[i][1]
    temp.append(a[i][1])
    if len(temp) > a[i][0]:
        temp.sort()
        total -= temp[0]
        temp.remove(temp[0])
print(total)