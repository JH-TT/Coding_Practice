n = list(input())

stick = 0
result = 0

while n: # n이 빌때까지 반복
    if n.pop() == ")":
        if n[-1] == "(": # 바로 괄호가 ()모양이면 자른다.
            n.pop()
            result += stick # n개의 막대를 한 번 자른다는것은 n개의 막대가 더 생긴다는 것.
        else:
            stick += 1 # 막대 1개 추가
            result += 1 # 결과값도 같이 1개 추가.
    else:
        stick -= 1

print(result)