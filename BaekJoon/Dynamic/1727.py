n, m = map(int, input().split())
man = list(map(int, input().split()))
w = list(map(int, input().split()))

man.sort()
w.sort()

def check(a, b): # a가 적은 인원, b가 많은 인원
    # p[i][j] i가 j번째까지 본 조합중에 최솟값을 저장.
    p = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(i, len(b)+1):
            if i == j: # 남, 여가 같은 수이면 이전값 + 현재 커플값 해준다.
                p[i][j] = p[i-1][j-1] + abs(a[i-1] - b[j-1])
            else: # 그렇지 않다면 솔로가 되거나 커플이 되거나 둘 중 하나.
                p[i][j] = min(p[i][j-1], p[i-1][j-1] + abs(a[i-1]-b[j-1]))
    return p[len(a)][len(b)]

if n >= m:
    print(check(w, man))
else:
    print(check(man, w))

# 자세한 설명 링크 : https://donggod.tistory.com/11 여기랑 알고리즘이 거의 같음.