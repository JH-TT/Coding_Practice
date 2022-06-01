# 1193 번

a = int(input())
b = 1  # 분자
c = 1  # 분모
s = 0  # 찾으려는 분수가 있는 바로 전 라인까지의 개수
count = 1
while True:
    s += count
    if s >= a:
        s -= count  # a번째 라인이 되면 그 전 라인 상태로 바꾼다.
        count -= 1
        break
    count += 1
d = a - s - 1  # 몇번째 라인까지 왔는지
if (count + 1) % 2 == 1: # 홀수 라인이면 분자가 증가하고 1씩 감소
    b += count
    for _ in range(d):
        b -= 1
        c += 1
else:
    c += count
    for _ in range(d):
        b += 1
        c -= 1
print(b, c, sep="/")