result = []
for i in range(int(input())):
    result.append(list(map(int, input().split())))

result = sorted(result, key = lambda x : (x[0], x[1])) # x좌표로 오름차순, 같으면 y순으로 정렬.

for i in result:
    print(i[0], i[1])