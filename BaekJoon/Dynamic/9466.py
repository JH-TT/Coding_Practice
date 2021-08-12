T = int(input())

for _ in range(T):
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:
        print(max(s[0][0], s[1][0]))
    elif n == 2:
        print(max(s[0][0] + s[1][1], s[1][0] + s[0][1]))
    else:
        s[0][1] += s[1][0]
        s[1][1] += s[0][0]
        for i in range(2, n):
            s[0][i] += max(s[1][i - 1], s[1][i - 2])
            s[1][i] += max(s[0][i - 1], s[0][i - 2])
        print(max(max(s[0]), max(s[1])))

# 인덱스가 0인것부터 차근차근 살펴보면 바로 규칙을 찾을 수 있었던 문제
# 길이가 3이상인것부터 살펴보면 인덱스가 3이상인 입장에서는 대각선 위 or 아래, 대각선 위 or 아래 왼쪽 둘 중에 큰 값을 더해줘야 한다는 것을 눈치챌 수 있게 된다.