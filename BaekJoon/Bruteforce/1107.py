n = int(input())
m = int(input())
if m:
    not_work = list(input().split())
else:
    not_work=[]

num = abs(n-100)
num_2 = ""

# n까지 수중에 적은 횟수로 누르는 경우 찾기
for i in range(n + 1):
    flag = True
    for j in str(i):
        if j in not_work:
            flag = False
            break
    if flag:
        num = min(num, abs(n - i) + len(str(i)))

# n+1부터 아까 구한 횟수만큼 탐색. 찾는 순간  그 수가 가장 적게 누르는 경우의 수가 된다.
for i in range(n + 1, n + num):
    flag = True
    for j in str(i):
        if j in not_work:
            flag = False
            break
    if flag:
        num = min(num, abs(n - i) + len(str(i)))
        break

print(num)

# 조건을 만족시키는 수중에 찾고자 하는 수와 차이가 가장 적은 숫자 찾기
# 찾으면 (아까 찾은 수 + 그 수의 길이) vs (+- 버튼만 눌렀을때 경우의 수)와 비교해서 최솟값 갱신