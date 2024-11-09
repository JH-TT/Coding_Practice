import sys
input = sys.stdin.readline


N = int(input())
arr = [[0 for _ in range(N + 1)]]

total = 0
for _ in range(N):
    sub = list(map(int, input().split()))
    arr.append([0] + sub)
    total += sum(sub)

res = 4000000
for x in range(1, N + 1):
    for y in range(1, N + 1):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                # 초반 범위에 들어가지 않으면 넘긴다. 1 ≤ x < x+d1+d2 ≤ N, 1 ≤ y-d1 < y < y+d2 ≤ N
                if not ((1 <= x < x + d1 + d2 <= N) and (1 <= y - d1 < y < y + d2 <= N)):
                    continue
                election = [[] for _ in range(5)]
                election[1] = [(x + i, y - i) for i in range(d1)]
                election[2] = [(x + i, y + i) for i in range(1, d2 + 1)]
                election[3] = [(x + d1 + i, y - d1 + i) for i in range(d2)]
                election[4] = [(x + d2 + i, y + d2 - i) for i in range(1, d1 + 1)]
                score = [0] * 6

                arr2 = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

                # 1번
                for r in range(1, election[1][0][0]):
                    for c in range(1, election[1][0][1] + 1):
                        score[1] += arr[r][c]
                for e in election[1]:
                    for c in range(1, e[1]):
                        score[1] += arr[e[0]][c]

                # 2번
                for r in range(1, election[2][0][0]):
                    for c in range(election[2][0][1], N + 1):
                        score[2] += arr[r][c]
                for e in election[2]:
                    for c in range(e[1] + 1, N + 1):
                        score[2] += arr[e[0]][c]

                # 3번
                for e in election[3]:
                    for c in range(1, e[1]):
                        score[3] += arr[e[0]][c]
                for r in range(election[3][-1][0] + 1, N + 1):
                    for c in range(1, election[3][-1][1] + 1):
                        score[3] += arr[r][c]

                # 4번
                for e in election[4]:
                    for c in range(e[1] + 1, N + 1):
                        score[4] += arr[e[0]][c]
                for r in range(election[4][-1][0] + 1, N + 1):
                    for c in range(election[4][-1][1], N + 1):
                        score[4] += arr[r][c]

                score[-1] = total - sum(score[1:-1])

                if max(score[1:]) - min(score[1:]) < res:
                    res = max(score[1:]) - min(score[1:])
print(res)

# 생각치 못한 부분에서 반례가 나와서 오래걸린 문제.... 구현자체는 어렵지 않았음