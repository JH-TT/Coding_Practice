a = list(input())
a.sort(reverse = True)
if a[-1] != "0":
    print(-1)
else:
    total = 0
    for i in a[:-1]:
        total += int(i)
    if total % 3 == 0:
        print(int("".join(a)))
    else:
        print(-1)

# 일단 30의 배수를 찾는거기 때문에, 0이 없으면 절대 30의 배수가 될 수 없다.
# 0이 있다면 0을빼고 나머지가 3의 배수인지 판별 후, 3의 배수가 아니면 -1 3의 배수면 내림차순 정렬한 수를 출력한다.
# 3의 배수 판별법 : 각 자릿수 합이 3의 배수면 3의 배수다.