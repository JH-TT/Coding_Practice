n = int(input())
m = int(input())
s = input()

total = 0
cnt = 0 # IOI의 개수
last = ""

for i in range(m):
    if last == "" and s[i] == "I":
        last = s[i]
    elif last == "I" and s[i] == "O":
        last = s[i]
    elif last == "O" and s[i] == "I":
        last = s[i]
        cnt += 1
    else:
        if cnt >= n:
            total += cnt - n + 1

        if s[i] == "I":
            last = s[i]
        else:
            last = ""
        cnt = 0

if cnt >= n:
    total += cnt - n + 1

print(total)

# total += cnt - n + 1 부분이 나오는 방식
# n이 2인데 IOIOIOIOI가 있다고 하자.
# 첫번째 I부터 P2인 IOIOI와 두 번째 I부터 P2, 세 번째 I 부터 P2 이렇게 3개가 나온다
# 즉, IO가 연속으로 나오는 경우, n이상부터는 IOI 패턴이 나오면 1씩 증가하는 셈이다.
# 굳이 KMP를 쓸 필요는... 연습정도로만 사용하면 될 듯 하다.