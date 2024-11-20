import sys
input = sys.stdin.readline

n, k = map(int, input().split())

stack = [0 for _ in range(k)]
meeting = []

for _ in range(n):
    meeting.append(list(map(int, input().split())))

meeting.sort(key = lambda x : (x[1], x[0]))

cnt = 0
for meet in meeting:
    stack.sort() # 최대 3개밖에 안되니 계속 정렬해도 된다.
    for i in range(k-1, -1, -1):
        if stack[i] < meet[0]:
            stack[i] = meet[1]
            cnt += 1
            break
print(cnt)

# 이 문제의 핵심은 (다음 회의 시작시간 - 이전 회의 끝시간)이 최소가 되어야 한다.
# 이걸 해결하는건 결국 정렬이 정답인데
# 저게 최소가 되려면 끝 시간 기준으로 먼저 정렬해야한다는 것을 느낄 수 있을것 이다.
# 어차피 시작시간은 끝 시간보다 작거나 같기 때문에 끝 시간만 정렬하면 시작시간은 이전 회의 끝 시간과 비교할때만 사용하면 된다.
# 만약 어떤 회의가 모든 회의실을 사용할 수 있다면 첫번째에 말한 조건을 생각해서 넣어야 한다.
# 그래서 for문이 돌때마다 stack을 정렬해서 뒤에서부터 비교를 시작한 것이다.