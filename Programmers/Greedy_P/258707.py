from collections import deque

def solution(coin, cards):
    answer = 1
    n = len(cards)
    exist = [0] * (len(cards) + 1) # 존재 여부
    no_coin = 0 # 코인 사용없이 만들 수 있는 개수

    original = deque()
    for i in range(n // 3):
        if exist[n - cards[i] + 1] == 1:
            exist[n - cards[i] + 1] = 0
            no_coin += 1
            continue
        exist[cards[i]] = 1
        original.append(cards[i])

    remain = deque()
    for i in range(n//3, n, 2):
        flag = False

        # 일단 2개의 카드를 등록해 놓는다.
        for j in range(2):
            h = i + j
            exist[cards[h]] = 1
            remain.append(cards[h])

        # 코인 없이 할 수 있으면 넘긴다.
        if no_coin > 0:
            no_coin -= 1
            answer += 1
            continue

        # 코인이 없으면 종료한다.
        if coin == 0: break

        # 코인 1개를 사용해야할 경우
        m = len(original)
        for _ in range(m):
            num = original.popleft() # 일단 하나를 꺼낸다.
            # 만약 한 개로 만들 수 있다면 다음 스테이지로
            if exist[n - num + 1] == 1:
                exist[num] = 0
                exist[n - num + 1] = 0
                coin -= 1
                flag = True # 성공
                answer += 1
                break
            original.append(num)
        if flag: continue

        # 코인 1개로도 만들수 없는데, coin도 1개 이하만 갖고 있으면 더이상 만들 수 없다.
        if coin < 2: break

        # 코인 2개를 사용해야할 경우
        m = len(remain)
        for _ in range(m):
            num2 = remain.popleft()
            if exist[num2] == 0: continue

            if exist[n - num2 + 1] == 1:
                exist[num2] = 0
                exist[n - num2 + 1] = 0
                coin -= 2
                flag = True
                answer += 1
                break
            remain.append(num2)

        # 코인은 충분하지만, 더이상 n+1을 만들 수 없다면 종료한다.
        if not flag: break


    return answer

# 이 문제는 조건을 만족하면 해당 값들을 버리고 다음 스테이지로 넘어가는 방식이다.
# 두개의 숫자를 합해서 n+1이 되면 조건을 충족하는건데, 이는 서로 다른 숫자라서 (a, b) 쌍은 전부 유니크하다.
# 따라서 중복관련된 부분은 생각할 필요는 없고, 조건을 만족하냐 안하냐 이정도만 확인하면 된다.
# 그래서 나는 해당 숫자들이 존재하는지 확인하는 exist와
# 숫자들을 처음부터 저장한 리스트와 스테이지 돌파로 인해 받는 2개의 숫자들을 넣는 리스트를 따로 구현했다.
# 여기서 최대한 많은 스테이지를 가는것이 목표 -> 이는 코인도 최대한 아끼는 것이 중요하다.
# 따라서 소비하는 코인의 개수를 기준으로 순서대로 쌍을 구하고 넘긴다. -> Greedy(그리디)하게 구현하는것이 관건
# 조건을 만족하지 못하거나, 코인이 부족하면 종료하는 방식으로 구현했다.