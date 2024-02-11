import sys
input = sys.stdin.readline

ESP = 1e-9

n = int(input())
score = sorted([int(input()) for _ in range(n)])
cut = round(n * 0.15 + ESP)
if n - cut * 2 == 0 or len(score) == 0: print(0)
else:
    mean = sum(score[cut:n-cut]) / (n - cut * 2)
    print(round(mean + ESP))

# 파이썬은 round의 경우 짝수.5 는 반올림 하면 짝수로 간다.
# 따라서 약간의 양수인 1e-9정도를 더해줘서 이러한 경우를 예방한다.

# 또는 정수를 뺀 뒤에 0.5로 비교하면 된다.