# 8958번 : "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

a = int(input())  # 몇번의 퀴즈를 볼 지
for i in range(a):
    s = 0  # 점수 초기화
    sum = 0  # 점수 합계 초기화
    b = input()  # OX를 입력받는다.
    for j in b: 
        if j == "O": # O면 s는 1증가하고, sum에다가 s를 더한다.
            s += 1
            sum += s
        else:  # X면 s는 0으로 초기화 된다.
            s = 0
    print(sum)