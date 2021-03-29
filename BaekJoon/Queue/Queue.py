import sys
input = sys.stdin.readline

n = int(input())
# 큐의 원리를 알면 딱히 설명이 필요없다.
ar = []
for _ in range(n):
    com = list(input().split()) # 리스트 형태로 입력받음. 리스트로 안하면 push는 정수도 같이 입력해야돼서 오류가 뜬다.
    if com[0] == "push":
        ar.append(com[1])
    elif com[0] == "pop":
        if len(ar) == 0:
            print(-1)
        else:
            print(ar.pop(0))
    elif com[0] == "size":
        print(len(ar))
    elif com[0] == "empty":
        if len(ar) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == "front":
        if len(ar) == 0:
            print(-1)
        else:
            print(ar[0])
    elif com[0] == "back":
        if len(ar) == 0:
            print(-1)
        else:
            print(ar[-1])