import sys
input = sys.stdin.readline

T = int(input())

case = [[0, 0, 0] for _ in range(100001)]
case[1] = [1, 0, 0]
case[2] = [0, 1, 0]
case[3] = [1, 1, 1]
case[4] = [2, 0, 1]

for i in range(5, 100001):
    for j in range(1, 4):
        case[i][j - 1] = (sum(case[i - j]) - case[i - j][j - 1]) % 1000000009

for _ in range(T):
    n = int(input())

    print(sum(case[n]) % 1000000009)

# 이 문제는 repl에서 풀면 메모리 초과가 뜬다.....
# 각 숫자들 만들때 맨 앞에 숫자가 나온 개수를 따로 저장한다. case[4]같은 경우응 1이 맨 앞인 경우 2개 3이 맨 앞인 경우 1개인 것이다.
# for문을 돌면서 i를 만들때 맨앞이 1인 경우 = i - 1을 만드는 모든 경우의 수 - i - 1을 만들때 맨 앞이 1인 경우 이런식으로 맨앞이 3인 경우까지 따로 계산해준다.
# 단 각 진행마다 10억9를 나눈 나머지를 넣어줘야한다. 값이 기하급수적으로 오르기때문에 시간초과가 뜬다. 파이썬인 경우 숫자 길이에 제한이 없지만, 숫자가 크면 연산속도도 느려지기 떄문이다.
# 따라서 다 계산후 마지막에만 10억9를 나눠주면 시간초과가 뜬다.

# 이 문제는 아이디어는 금방 떠올랐지만 repl에서 계속 실행이 안되어 잘못짠줄 알고 끙끙댄 문제.... repl을 계속 써야하나....