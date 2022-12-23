a, b = map(int, input().split())
diff = b - a
if a == b:
    print(0)
    exit()
i = 1
while 1:
    if i**2 + i >= diff:
        break
    i += 1
if (diff - (i**2 - i)) <= i:
    print(2*i-1)
else:
    print(2*i)

# 하나씩 확인해보면 일정한 규칙이 생긴다
# 1
# 1 1
# 1 1 1
# 1 2 1
# ... 이런식으로 그리다 보면 일(day)수가 1, 1, 2, 2, 3, 3, 4, 4 ... 이 된다는것을 알 수 있다.