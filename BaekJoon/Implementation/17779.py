# # d1, d2 >= 1
# # 1 <= x < x + d1 + d2 <= N
# # 1 <= y-d1 < y <= y+d2 <= N

N = int(input())
A = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]

res = 400000
# x, y, d1, d2를 미리 정한다.
for x in range(1, N+1):
    for y in range(1, N+1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if not (1 <= x < x + d1 + d2 <= N and 1 <= y-d1 < y < y+d2 <= N):
                    continue
                score = [0] * 6
                for r in range(1, N+1):
                    for c in range(1, N+1):
                        if 1 <= r < x+d1 and 1 <= c <= y:
                            if r < -c + x + y:
                                score[1] += A[r][c]
                                continue
                        if 1 <= r <= x+d2 and y < c <= N:
                            if r < c + x - y:
                                score[2] += A[r][c]
                                continue
                        if x+d1 <= r <= N and 1 <= c < y-d1+d2:
                            if r > c + x - y + 2 * d1:
                                score[3] += A[r][c]
                                continue
                        if x+d2 < r <= N and y-d1+d2 <= c <= N:
                            if r > -c + x + y + 2 * d2:
                                score[4] += A[r][c]
                                continue
                        score[5] += A[r][c]
                res = min(res, max(score[1:]) - min(score[1:]))
print(res)

# 기울기가 1 또는 -1이기 때문에 (r, c)를 지나는 직선을 그리고 2*d1 과 2*d2만큼 평행이동시키면 4개의 직선들이 이루는 사각형내부가 지역 5가 된다.
# 그래서 5를 제외한 나머지는 1, 2, 3, 4이므로 따로 구하고 마지막에 최댓값 - 최솟값을 해서 산출했다.

# 다른 사람 풀이
# 이 풀이는 슬라이싱을 이용해서 푼 문제다. 
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total = sum([sum(row) for row in arr])
ans = 1e9

# 1구역 구하기
def findOne(x, y, d1):
    one = 0
    for row in arr[:x]:
        one += sum(row[:y+1])
    
    for i in range(d1):
        one += sum(arr[x+i][:y-i])
    
    return one

# 2구역 구하기
def findTwo(x, y, d2):
    two = 0
    for row in arr[:x+1]:
        two += sum(row[y+1:])
    
    for i in range(1, d2+1):
        two += sum(arr[x+i][y+i+1:])

    return two

# 3구역 구하기
def findThree(x, y, d1, d2):
    three = 0
    for i in range(d2+1):
        three += sum(arr[x+d1+i][:y-d1+i])

    for row in arr[x+d1+d2+1:]:
        three += sum(row[:y-d1+d2])

    return three

# 4구역 구하기
def findFour(x, y, d1, d2):
    four = 0

    for i in range(1, d1+1):
        four += sum(arr[x+d2+i][y+d2-i+1:])

    for row in arr[x+d1+d2+1:]:
        four += sum(row[y-d1+d2:])
    
    return four

# 1~5구역 인구수 구해서 리스트로 만들고 최대 - 최소 값 반환하기
def Ward(x, y, d1, d2):
    ward = [findOne(x, y, d1), findTwo(x, y, d2), findThree(x, y, d1, d2), findFour(x, y, d1, d2)]
    ward.append(total-sum(ward))
    return max(ward)-min(ward)

for x in range(N-2):
    for y in range(1, N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x+d1+d2>=N or y-d1<0 or y+d2>=N:
                    continue
                # t = Ward(x, y, d1, d2)
                # if ans > t:
                #     ans = t
                ans = min(ans, Ward(x, y, d1, d2)) # 주석처리된 코드를 한 줄로 표현하면 이렇게 된다. 

print(ans)

# 좌표만 보면 함수를 생각하다 보니 비교적 어렵게 접근했던거 같다.