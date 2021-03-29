import sys
input = sys.stdin.readline

n = int(input())

a = [] # 수열들을 저장
b = [] # 1부터 n까지 상황에따라 push, pop하는 곳
c = [] # push면 +, pop이면 -를 저장하는 공간.

for _ in range(n):
    a.append(int(input()))
j = 1
for i in a:
    if i >= j: # 입력된 수가 더 큰 경우.
        for _ in range(j, i + 1): # j부터 i까지 계속 입력 후
            b.append(j)
            c.append("+") 
            j += 1
        b.pop() # 마지막껀 빼준다.
        c.append("-")
    else: # j가 더 큰 경우.(이미 i는 저장돼 있을 수 있음)
        if b[-1] == i: # b의 마지막이 i이면
            b.pop()
            c.append("-")
        else: # 아닌경우엔 a수열로 만들 수 없다.
            c.append("n")
if "n" in c:
    print("NO")
else:
    for h in c:
        print(h)
# 이 문제는 원리는 알았는데 코드로 구현하는데 조금 부족한 면이 없지않아 있었다. 좀 더 깊게 생각하고 구현하길 노력해야 한다.