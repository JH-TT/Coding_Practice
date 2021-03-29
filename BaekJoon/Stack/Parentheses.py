import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    v = list(input())
    v.pop() # \n 제거.
    b = []
    if len(v) % 2 == 1: # 문자열 길이가 홀수면 짝이 안맞으니 바로 NO라고 출력
        print("NO")
        continue # 바로 다음 테스트로 넘어감.
    else:
        while len(v) > 0: # v가 빌때까지 반복
            t = v.pop() # 일단 v에서 뽑고
            if t == ")": # ) 인 경우는 무조건 b리스트에 넣기만함.
                b.append(t)
            else:
                if len(b) > 0 and b[-1] == ")": # "(" 인 경우엔 b의 top이 ")" 인지 보기.
                    b.pop() # ) 이면 짝을 이루니 b에서 pop함.
                else:
                    b.append(t) # 아닌경우엔 넣음.
    if len(b) > 0: # b가 비어있지 않으면 짝을 다 못 이룬거니 NO 출력
        print("NO")
    else:
        print("YES")