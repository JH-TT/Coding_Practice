def trans(a):
    b = []
    for i in range(len(a[0])):
        c = []
        for j in range(len(a)):
            c.append(a[j][i])
        b.append(c)

    return b

def R_calc(a):
    D = []
    for i in a:
        F = []
        for j in set(i):
            if j == 0:
                continue
            F.append([j, i.count(j)])
        F.sort(key=lambda x : (x[1], x[0]))
        D.append(F)
    G = []
    for i in D:
        H = []
        for j in i:
            H.extend(j)
        G.append(H)
    
    M_length = max(len(x) for x in G)
    for i in G:
        length = M_length - len(i)
        i.extend([0] * length)
    return G


def C_calc(a):
    a = trans(a)
    a = R_calc(a)
    return trans(a)

r, c, k = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(3)]

timer = 0

while timer <= 100:
    R = len(A)
    C = max(len(x) for x in A)
    
    if 0 <= r-1 < len(A) and 0 <= c-1 < len(A[0]):
        if A[r-1][c-1] == k:
            print(timer)
            exit()
    if R >= C:
        A = R_calc(A)
    else:
        A = C_calc(A)
    
    if len(A) >= 100:
        A = A[:100]
    A = [x[:100] for x in A]

    timer += 1
print(-1)