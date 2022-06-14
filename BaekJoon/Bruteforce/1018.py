ans = 2500

n, m = map(int, input().split())

chess = [input() for _ in range(n)]

# 시작이 BW순인 경우
black = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
# 시작이 WB순인 경우
white = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]

# 부르트포스 실행
for i in range(n-7):
    for j in range(m-7):
        b = 0
        w = 0
        for h in range(i, i+8):
            for k in range(j, j+8):
                if chess[h][k] != black[h-i][k-j]:
                    b += 1
                if chess[h][k] != white[h-i][k-j]:
                    w += 1
        ans = min(ans, min(b, w))
print(ans)