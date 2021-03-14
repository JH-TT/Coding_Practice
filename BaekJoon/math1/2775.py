# python은 시간초과, pypy3은 성공.
def bb(a, b): # 재귀함수 이용.
    if a == 0: # 0층은 사람 사는 수가 b명.
        return b
    elif b == 1: # b호는 전부 1명
        return 1
    else:
        return bb(a - 1, b) + bb(a, b - 1) # 그 외에는 (옆호에 사는 사람수) + (바로 아랫층 사람수)

n = int(input()) # 테스트 케이스

for _ in range(n):
    a = int(input()) # 층
    b = int(input()) # 호
    print(bb(a, b))

# Python 성공
n = int(input()) # 테스트 케이스

for _ in range(n):
    a = int(input())
    b = int(input())
    l = [] # 1층부터 사람수를 저장할 공간.
    m = [[(x + 1) for x in range(b)]] # 0층은 호수가 사람수.
    for i in range(a):
        for j in range(b):
            l.append(sum(m[i][:j + 1])) # (a - 1)층에 각 호수마다 사는 사람 수 저장.
        m.append(l) # 이걸 0층정보가 있는 리스트에 저장
        l = [] # 넣었으니 다시 비운다.
    print(m[a][b - 1]) # 찾고자 하는 사람 수.