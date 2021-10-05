arr = list(input())
total = []

if len(arr) % 2 == 1: # 홀수개는 무조건 0출력
    print(0)
    exit(0)

while arr: # arr이 빌때까지 반복.

    # 괄호 한 쌍이 있으면 그에 맞는 수를 total에 넣음.
    if len(arr) > 1 and arr[-1] == ")" and arr[-2] == "(":
        total.append(2)
        arr.pop()
        arr.pop()
    elif len(arr) > 1 and arr[-1] == "]" and arr[-2] == "[":
        total.append(3)
        arr.pop()
        arr.pop()
    else:
        if arr[-1] == "(":
            arr.pop()
            num = 0
            while total and total[-1] != ")": # total이 비어있지않고, )가 나올때까지 반복.
                try:
                    num += total.pop()
                except: # 오류발생시, 쌍이 안맞는거.
                    print(0)
                    exit(0)
            if not total: # 끝까지 ) 가 없는 경우 쌍이 안맞음.
                print(0)
                exit(0)
            total.pop()          
            total.append(num * 2)
        elif arr[-1] == "[":
            arr.pop()
            num = 0
            while total and total[-1] != "]":
                try:
                    num += total.pop()
                except:
                    print(0)
                    exit(0)
            if not total:
                print(0)
                exit(0)                    
            total.pop()                    
            total.append(num * 3)
        else:
            total.append(arr.pop())
try: # 중간에 문자가 있으면 0출력.
    print(sum(total))
except:
    print(0)