import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

if sum(arr) % 4:
    print(0)
else:
    cnt = [1] + [0] * 3
    s = 0
    aim = sum(arr) // 4
    for i in range(n-1):
        s += arr[i]
        if s == 3 * aim:
            cnt[3] += cnt[2]
        if s == 2 * aim:
            cnt[2] += cnt[1]
        if s == aim:
            cnt[1] += cnt[0]
    print(cnt[3])

# 참고사이트 : https://velog.io/@redcarrot01/ProblemSolving-%EB%B0%B1%EC%A4%80-21757-%EB%82%98%EB%88%84%EA%B8%B0-dp
# 참고사이트 : https://tedcho.tistory.com/26