import sys
input = sys.stdin.readline

num = []
n = int(input())
for _ in range(n):
    num.append(int(input()))
num.sort()
res = sys.maxsize
start = 0
end = 0
while end < n:
    if num[end] - num[start] < 4: # 아직 더 봐야하는 상황
        end += 1
    elif num[end] - num[start] == 4: # 딱 현재 숫자가 연속된 숫자중 가장 큰 숫자인 경우
        res = min(res, 5-(end-start+1)) # 5 - (start원소 + end원소 + 사이 원소)
        start = end
    else: # 현재 숫자가 첫번째 숫자보다 5이상 차이나는 경우.
        res = min(res, 5-(end-start)) # # 5 - (start원소 + 사이 원소), end 원소는 너무 커서 그 라인에 못들어감
        start = end
print(min(res, 5-(end-start))) # 다 확인하고 남은 라인이 있는지 확인