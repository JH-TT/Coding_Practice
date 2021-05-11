n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
for i in coin:
    # 만들 수 없는 금액을 찾았을 때 반복 종료    # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < i:
                break
                    target += i

                    print(target)
    if target < i:
        break
    target += i

print(target)

# 이 알고리즘은 생각하지 못했다.
# 나는 1부터 1씩 증가시키면서 그 금액을 만들 수 있는지 판단하는 방식으로 했는데 이 정답 알고리즘은 좀 다르다.

# 먼저, 금액 1을 만들 수 있는지 확인위해, target = 1로 설정 그 전에 동전들은 오름차순 정렬해 놓음
# 화폐단위가 1인 동전이 있으면 target에 금액1을 더해서 2로 만든다(이 의미는 현재 갖고 있는 동전으로 1원까지는 만들 수 있다는 얘기.)
# target = 2인데 이때 2인 동전이 있다면 또 더한다. target = 4(3까진 만들 수 있다.)
# 이런식으로 계속 해서 만약 target이 다음에 오는 동전보다 작으면 종료. target출력(그 금액을 만들 수 없다는 얘기.)