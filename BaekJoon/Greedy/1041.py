# 1면 -> 6(n-2)**2
# 2면 -> 12(n-2) 
# 3면 -> 8
# 위는 n이 2이상일 경우에만 성립된다.
INF = 10**9
three = [[0, 1, 2], [0, 2, 4], [0, 3, 4], [0, 1, 3],
         [2, 4, 5], [2, 1, 5], [1, 3, 5], [3, 4, 5]]
two = [[0, 1], [0, 2], [0, 3], [0, 4],
       [1, 2], [1, 3], [2, 4], [3, 4],
       [1, 5], [2, 5], [3, 5], [4, 5]]

n = int(input())
dice = list(map(int, input().split()))

if n == 1:
    print(sum(dice) - max(dice))
    exit(0)

three_case = [INF, INF]
two_case = [INF, INF]
one_case = min(dice)

for a, b, c in three:
    total = sum([dice[a], dice[b], dice[c]])
    max_ = max([dice[a], dice[b], dice[c]])
    if total < three_case[0]:
        three_case = [total, max_]
    elif total == three_case[0]:
        if max_ > three_case[1]:
            three_case = [total, max_]

for a, b in two:
    total = sum([dice[a], dice[b]])
    max_ = max(dice[a], dice[b])
    if total < two_case[0]:
        two_case = [total, max_]
    elif total == two_case[0]:
        if max_ > two_case[1]:
            two_case = [total, max_]

# 최종값
# 1개짜리는 값이 같으니까 한번에 밑면의 개수는 뺀다.
# 2, 3개짜리는 거기중에 가장 큰 값을 더해서 빼준다.        

all_total = one_case * 5 * (n-2) ** 2 + two_case[0] * 12 * (n-2) + three_case[0] * 8
one_part_total = three_case[1] * 4 + two_case[1] * 4 * (n-2)
print(all_total - one_part_total)