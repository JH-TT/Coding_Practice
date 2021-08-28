import sys
input = sys.stdin.readline

n = int(input())

Flower = [list(map(int, input().split())) for _ in range(n)]
Flower.sort(key=lambda x : (x[0], x[1], x[2], x[3])) # 일단 미리 정렬을 해 둔다.

start = [] # 피는시점
end = [] # 지는시점

for i in range(n):
    a, b, c, d = Flower[i]
    start.append(a * 100 + b) # 3월 4일이면 304로 저장
    end.append(c * 100 + d)

cnt = 0 # 꽃의 개수
month_day = 301

# 예외처리
if start[0] > 301: # 가장 먼저피는 날짜가 3/1 이후
    print(0)
    exit(0)
elif end[-1] <= 1130: # 가장 늦게지는 날짜가 11/30이전(11/30 포함) -> 피는날짜가 a고 지는날짜가b면 꽃이 존재하는 기간은 a <= x < b이다.
    print(0)
    exit(0)

index = 0
for i in range(n):
    # 피는날짜가 month_day이후이면, 현재꽃 이전에 꽃들중에 가장 늦게 지는 날짜를 month_day로 두고 cnt 1증가.
    if i < n - 1 and start[i + 1] > month_day:
        month_day = max(month_day, max(end[index:i+1]))
        index = i+1
        cnt += 1
        # 만약 3/1 ~ 11/30중에 하루라도 꽃이 없는 경우가 나오면 0출력 후 종료.
        if month_day < start[index]:
            print(0)
            exit(0)
    # 11/30이후에 지면 cnt출력후 종료
    if month_day > 1130:
        print(cnt)
        exit(0)
# 여기까지 종료없이 빠져나온거는 모든 꽃의 피는날짜가 month_day보다는 이전인 경우에 빠져나온다. (백준사이트 2457문제 첫번쨰 TC참고)
# 그럴땐 나머지중에 가장 늦게 지는 날짜를 month_day로 지정후 cnt 1증가.
if month_day < max(end[index:]):
    month_day = max(end[index:])
    cnt += 1

print(cnt if month_day > 1130 else 0) # month_day가 11월30일 이후면 cnt출력 아니면 0출력.

# 문제자체는 어렵지 않았으나, 사소한 실수로 시간을 많이 잡아먹었음. 메모리도 좀 많이 먹은 편인듯하다.