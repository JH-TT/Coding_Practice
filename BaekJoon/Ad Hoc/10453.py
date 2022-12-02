for _ in range(int(input())):
    A, B = input().split()
    lenA = A[1:-1].count("a")
    lenB = B[1:-1].count("a")
    if len(A) == 2 and len(B) == 2:
        print(0)
        continue
    # 절대 맞출 수 없는 경우.(길이가 안맞거나 a혹은 b의 개수가 안맞거나)
    if len(A) != len(B):
        print(-1)
        continue
    if lenA != lenB:
        print(-1)
        continue
    # 맞출 수 있는 경우
    # A에서 a혹은 b가 B로의 a혹은 b까지의 거리를 계산한다.
    a = []
    b = []
    for i in range(len(A)):
        if A[i] == "a":
            a.append(i)
        if B[i] == "a":
            b.append(i)
    print(sum([abs(a[i] - b[i]) for i in range(len(a))]))

# 주석으로 설명해 놓음