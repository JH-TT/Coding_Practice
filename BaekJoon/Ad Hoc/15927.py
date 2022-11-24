import math

pal = input()
n = len(pal)
if pal == pal[0] * n:
    print(-1)
elif pal[:n//2][::-1] == pal[math.ceil(n/2):]:
    print(n-1)
else:
    print(n)

# 아이디어
# 전부 같은 문자 또는 길이가 1이면 무조건 -1
# 그 외에는 회문인지 확인을 하는데
# 만약 pal자체가 회문이면 pal의 길이 - 1 이 답이된다.(전부 같은 문자는 이전에 거르기때문)
# 회문이 아니면 pal길이 자체가 답이다.

# 처음에 아이디어는 거의 접근했는데 전부 같은 문자 또는 길이가 1인 경우를 따로 분리를 안해서 시간초과뜸 (ex O가 50만개면 시간초과뜰거임)